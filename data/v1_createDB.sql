-- TABLES
PRAGMA foreign_keys = true;

-- TODO 1.3 : Créer les tables manquantes et modifier celles ci-dessous

CREATE TABLE IF NOT EXISTS Spectacle (
    noSpec          INTEGER         PRIMARY KEY,
    nomSpec         VARCHAR(64)     NOT NULL        UNIQUE,
    prixBaseSpec    DECIMAL(6, 2)   NOT NULL,
    CHECK (prixBaseSpec >= 0)
);

CREATE TABLE IF NOT EXISTS Representation (
    noRep           INTEGER         PRIMARY KEY,
    noSpec          INTEGER         NOT NULL,
    dateRep         DATE            NOT NULL,
    promoRep        DECIMAL(4, 2)   NOT NULL        DEFAULT 0,
    CHECK (promoRep >= 0 AND promoRep <= 1),
    FOREIGN KEY (noSpec) REFERENCES Spectacle(noSpec) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Categorie (
    catZone         VARCHAR(32)     PRIMARY KEY,
    tauxZone        DECIMAL(4, 2)   NOT NULL,
    CHECK (tauxZone >= 1 AND tauxZone <= 2),
    CHECK (catZone IN ('orchestre', 'balcon', 'poulailler'))
);

CREATE TABLE IF NOT EXISTS Zone (
    noZone          INTEGER         PRIMARY KEY,
    catZone         VARCHAR(32)     NOT NULL        UNIQUE,
    FOREIGN KEY (catZone) REFERENCES Categorie(catZone) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Place (
    noPlace         INTEGER         NOT NULL,
    noRang          INTEGER         NOT NULL,
    noZone          INTEGER         NOT NULL,
    CONSTRAINT pk_place_noRang_noPlace PRIMARY KEY (noRang, noPlace),
    FOREIGN KEY (noZone) REFERENCES Zone(noZone) ON DELETE CASCADE,
    CHECK (noPlace > 0),
    CHECK (noRang > 0)
);

CREATE TABLE IF NOT EXISTS Reduction (
    typeReduc       VARCHAR(32)     NOT NULL        UNIQUE,
    tauxReduc       DECIMAL(4, 2)   NOT NULL,
    CHECK (typeReduc IN ('sans reduction', 'adherent', 'scolaire', 'etudiant', 'militaire', 'senior')),
    CHECK (tauxReduc >= 0 AND tauxReduc <= 1)
);

CREATE TABLE IF NOT EXISTS Vente (
    noAchat         INTEGER         PRIMARY KEY,
    dateAchat       DATE            NOT NULL,
    noRep           INTEGER         NOT NULL,
    FOREIGN KEY (noRep) REFERENCES Representation(noRep) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Ticket (
    noTicket        INTEGER         PRIMARY KEY,
    noAchat         INTEGER         NOT NULL,
    noRang          INTEGER         NOT NULL,
    noPlace         INTEGER         NOT NULL,
    prixTotal       DECIMAL(6, 2)   NOT NULL,
    typeReduc       VARCHAR(32)     NOT NULL,
    FOREIGN KEY (noAchat) REFERENCES Vente(noAchat) ON DELETE CASCADE,
    FOREIGN KEY (noPlace, noRang) REFERENCES Place(noPlace, noRang) ON DELETE CASCADE,
    FOREIGN KEY (typeReduc) REFERENCES Reduction(typeReduc) ON DELETE CASCADE
);





-- VIEWS

-- TODO 1.4 : Créer une vue LesRepresentations ajoutant le nombre de places disponible et d'autres possibles attributs calculés.

CREATE VIEW IF NOT EXISTS LesRepresentations AS
    WITH places AS (
        SELECT COUNT(noPlace) AS totalNbPlaces
            FROM Place
    ),
    tickets AS (
        SELECT noAchat, noTicket, noRep
            FROM Ticket
            LEFT JOIN Vente USING(noAchat)
    )
    SELECT nomSpec, noRep, dateRep, promoRep, (totalNbPlaces - COUNT(noTicket)) AS nbPlacesDisponibles, COUNT(noTicket) AS nbPlacesOccupees
    FROM Spectacle
        LEFT JOIN Representation USING(noSpec)
        LEFT JOIN tickets USING(noRep)
        LEFT JOIN places
    WHERE noSpec IN (
        SELECT noSpec
            FROM Representation
    )
    GROUP BY nomSpec, dateRep;


-- TODO 1.5 : Créer une vue  avec le noDos et le montant total correspondant.
CREATE VIEW IF NOT EXISTS LesVentes AS
    SELECT noAchat, SUM(prixTotal) AS montantTotal
    FROM Ticket
        LEFT JOIN Vente USING(noAchat)
    GROUP BY noAchat;


-- TODO 3.3 : Ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)

-- fait dans v1_createTriggers.sql