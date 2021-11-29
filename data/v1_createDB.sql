-- TODO 1.3 : Créer les tables manquantes et modifier celles ci-dessous

-- Primary key par defaut a un NOT NULL. Inutile de le preciser donc.

-- TABLES

CREATE TABLE Spectacle (
    noSpec          INTEGER         PRIMARY KEY,
    nomSpec         VARCHAR(64)     NOT NULL,
    prixBaseSpec    DECIMAL(6, 2)   NOT NULL,
    CHECK (prixBaseSpec >= 0)
);

CREATE TABLE Representation (
    noRep           INTEGER         PRIMARY KEY,
    dateRep         DATE            NOT NULL,
    promoRep        DECIMAL(4, 2)   NOT NULL        DEFAULT 0,
    CHECK (promoRep >= 0 AND promoRep <= 1)
);

CREATE TABLE Categorie (
    catZone         VARCHAR(32)     PRIMARY KEY,
    tauxZone        DECIMAL(4, 2)   NOT NULL,
    CHECK (tauxZone >= 0 AND tauxZone <= 1),
    CHECK (catZone IN ('orchestre', 'balcon', 'poulailler'))
);

CREATE TABLE Zone (
    noZone          INTEGER         PRIMARY KEY,
    catZone         VARCHAR(32)     NOT NULL        UNIQUE,
    FOREIGN KEY (catZone) REFERENCES Categorie(catZone)
);

CREATE TABLE Place (
    noRang          INTEGER         NOT NULL        UNIQUE,
    noPlace         INTEGER         NOT NULL,
    noZone          INTEGER         NOT NULL,
    CONSTRAINT pk_place_noRang_noPlace PRIMARY KEY (noRang, noPlace)
);

CREATE TABLE Reduction (
    typeReduc       VARCHAR(32)     NOT NULL        UNIQUE,
    tauxReduc       DECIMAL(4, 2)   NOT NULL,
    CHECK (typeReduc IN ('adhérent', 'senior', 'étudiant', 'sans reduction'))
);


CREATE TABLE Ticket (
    noTicket        INTEGER         NOT NULL,
    noAchat         INTEGER         NOT NULL,
    dateAchat       DATE            NOT NULL,
    noRep           INTEGER         NOT NULL,
    noRang          INTEGER         NOT NULL,
    noPlace         INTEGER         NOT NULL,
    CONSTRAINT pk_ticket_noTicket_noAchat PRIMARY KEY (noTicket, noAchat),
    FOREIGN KEY (noRep) REFERENCES Representation(noRep),
    FOREIGN KEY (noRang) REFERENCES Place(noRang),
    FOREIGN KEY (noPlace) REFERENCES Place(noPlace)
);

CREATE TABLE Vente (
    noAchat         INTEGER         PRIMARY KEY,
    prixGlobal      DECIMAL(6, 2)   NOT NULL,
    typeReduc       VARCHAR(32)     NOT NULL,
    FOREIGN KEY (typeReduc) REFERENCES Reduction(typeReduc)
);




-- VIEWS



-- TODO 1.4 : Créer une vue LesRepresentations ajoutant le nombre de places disponible et d'autres possibles attributs calculés.
-- TODO 1.5 : Créer une vue  avec le noDos et le montant total correspondant.
-- TODO 3.3 : Ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)