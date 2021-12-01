---------------------- TRANSFERT FROM V0 TO V1

INSERT INTO Spectacle(nomSpec, prixBaseSpec)
    SELECT DISTINCT nomSpec, prixBaseSpec
    FROM V0_LesRepresentations;

INSERT INTO Representation(noSpec, dateRep, promoRep)
    SELECT noSpec, dateRep, promoRep
    FROM V0_LesRepresentations;

INSERT INTO Categorie(catZone, tauxZone)
    SELECT DISTINCT catZone, tauxZone
    FROM V0_LesPlaces;

INSERT INTO Zone(catZone)
    SELECT catZone
    FROM Categorie;

INSERT INTO Place(noPlace, noRang, noZone)
    SELECT noPlace, noRang, noZone
    FROM V0_LesPlaces;


-- V1

---------------------- REDUCTION
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES
    ('adherent', 0.2),
    ('senior', 0.3),
    ('militaire', 0.3),
    ('etudiant', 0.5),
    ('scolaire', 0.5),
    ('sans reduction', 0);

---------------------- VENTE
INSERT INTO Vente(dateAchat) VALUES
    ('20/12/2019 18:53'),
    ('19/12/2019 12:02'),
    ('15/12/2019 17:05'),
    ('13/12/2019 16:45');

---------------------- TICKET // need vente + place + representation + reduction
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace, prixTotal, typeReduc) VALUES
    (1, 1, 1, 1, 37.5, 'etudiant'),
    (1, 1, 1, 2, 37.5, 'etudiant'),
    (1, 1, 1, 3, 37.5, 'etudiant'),
    (2, 1, 3, 4, 26.25, 'senior'),
    (3, 2, 3, 5, 20, 'sans reduction'),
    (4, 2, 2, 1, 32, 'adherent');