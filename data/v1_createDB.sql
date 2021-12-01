-- TABLES

-- TODO 1.3 : Créer les tables manquantes et modifier celles ci-dessous

CREATE TABLE Spectacle (
    noSpec          INTEGER         PRIMARY KEY,
    nomSpec         VARCHAR(64)     NOT NULL        UNIQUE,
    prixBaseSpec    DECIMAL(6, 2)   NOT NULL,
    CHECK (prixBaseSpec >= 0)
);

CREATE TABLE Representation (
    noRep           INTEGER         PRIMARY KEY,
    noSpec          INTEGER         NOT NULL,
    dateRep         DATE            NOT NULL,
    promoRep        DECIMAL(4, 2)   NOT NULL        DEFAULT 0,
    CHECK (promoRep >= 0 AND promoRep <= 1),
    FOREIGN KEY (noSpec) REFERENCES Spectacle(noSpec)
);

CREATE TABLE Categorie (
    catZone         VARCHAR(32)     PRIMARY KEY,
    tauxZone        DECIMAL(4, 2)   NOT NULL,
    CHECK (tauxZone >= 1 AND tauxZone <= 2),
    CHECK (catZone IN ('orchestre', 'balcon', 'poulailler'))
);

CREATE TABLE Zone (
    noZone          INTEGER         PRIMARY KEY,
    catZone         VARCHAR(32)     NOT NULL        UNIQUE,
    FOREIGN KEY (catZone) REFERENCES Categorie(catZone)
);

CREATE TABLE Place (
    noPlace         INTEGER         NOT NULL,
    noRang          INTEGER         NOT NULL,
    noZone          INTEGER         NOT NULL,
    CONSTRAINT pk_place_noRang_noPlace PRIMARY KEY (noRang, noPlace),
    FOREIGN KEY (noZone) REFERENCES Zone(noZone),
    CHECK (noPlace > 0),
    CHECK (noRang > 0)
);

CREATE TABLE Reduction (
    typeReduc       VARCHAR(32)     NOT NULL        UNIQUE,
    tauxReduc       DECIMAL(4, 2)   NOT NULL,
    CHECK (typeReduc IN ('adherent', 'senior', 'militaire', 'etudiant', 'scolaire', 'sans reduction')),
    CHECK (tauxReduc >= 0 AND tauxReduc <= 1)
);

CREATE TABLE Vente (
    noAchat         INTEGER         PRIMARY KEY,
    dateAchat       DATE            NOT NULL,
    prixGlobal      DECIMAL(6, 2)   NOT NULL,
    typeReduc       VARCHAR(32)     NOT NULL,
    FOREIGN KEY (typeReduc) REFERENCES Reduction(typeReduc)
);

CREATE TABLE Ticket (
    noTicket        INTEGER         PRIMARY KEY,
    noAchat         INTEGER         NOT NULL,
    noRep           INTEGER         NOT NULL,
    noRang          INTEGER         NOT NULL,
    noPlace         INTEGER         NOT NULL,
    FOREIGN KEY (noAchat) REFERENCES Vente(noAchat),
    FOREIGN KEY (noRep) REFERENCES Representation(noRep),
    FOREIGN KEY (noRang) REFERENCES Place(noRang),
    FOREIGN KEY (noPlace) REFERENCES Place(noPlace)
);





-- VIEWS

-- TODO 1.4 : Créer une vue LesRepresentations ajoutant le nombre de places disponible et d'autres possibles attributs calculés.
CREATE VIEW LesRepresentations AS
    SELECT nomSpec, dateRep, (500 - count(noTicket)) AS nbPlaceDisponibles, count(noTicket) AS nbPlacesOccupees
    FROM Spectacle
        LEFT JOIN Representation USING (noSpec)
        LEFT JOIN Ticket USING (noRep)
    GROUP BY nomSpec, dateRep;


-- TODO 1.5 : Créer une vue  avec le noDos et le montant total correspondant.
-- TODO 3.3 : Ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)