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
    ('sans reduction', 0),
    ('adherent', 0.2),
    ('scolaire', 0.5),
    ('etudiant', 0.5),
    ('militaire', 0.3),
    ('senior', 0.3);

---------------------- VENTE
INSERT INTO Vente(dateAchat, noRep) VALUES
    ('13/12/2022 16:45', 2),
    ('15/12/2022 17:05', 2),
    ('19/12/2022 12:02', 1),
    ('20/12/2022 18:53', 1);

---------------------- TICKET // need vente + place + representation + reduction
INSERT INTO Ticket(noAchat, noRang, noPlace, prixTotal, typeReduc) VALUES
    (1, 1, 1, 37.5, 'etudiant'),
    (1, 1, 2, 37.5, 'etudiant'),
    (1, 1, 3, 37.5, 'etudiant'),
    (2, 3, 4, 26.25, 'senior'),
    (3, 3, 5, 20, 'sans reduction'),
    (4, 2, 1, 32, 'adherent');