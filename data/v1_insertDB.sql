-- TRANSFERT FROM V0 TO V1

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

---------------------- REDUCTION
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('adherent', 0.2);
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('senior', 0.3);
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('militaire', 0.3);
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('etudiant', 0.5);
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('scolaire', 0.5);
INSERT INTO Reduction(typeReduc, tauxReduc) VALUES ('sans reduction', 0);
---------------------- VENTE // need reduction
INSERT INTO Vente(dateAchat, prixGlobal, typeReduc) VALUES('20/12/2019 18:53', 37.5, 'etudiant');
INSERT INTO Vente(dateAchat, prixGlobal, typeReduc) VALUES('19/12/2019 12:02', 26.25, 'senior');
INSERT INTO Vente(dateAchat, prixGlobal, typeReduc) VALUES('15/12/2019 17:05', 20, 'sans reduction');
INSERT INTO Vente(dateAchat, prixGlobal, typeReduc) VALUES('13/12/2019 16:45', 32, 'adherent');
---------------------- TICKET // need vente + place + representation
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(1, 1, 1, 1);
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(1, 1, 1, 2);
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(1, 1, 1, 3);
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(2, 1, 3, 4);
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(3, 2, 3, 5);
INSERT INTO Ticket(noAchat, noRep, noRang, noPlace) VALUES(4, 2, 2, 1);