--------------------- SPECTACLE
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (1, 'Anne Rasse x Laurence Pierre', 20);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (2, 'Javascript c la vi', 10);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (3, 'UE5 > Unity', 150);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (4, 'Java ca pue', 2000);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (5, 'Je suis maitrise 7 sur Yasuo et Yi', 0);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (6, 'Javascript c la vi', 10);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (7, 'UE5 > Unity', 150);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (8, 'Java ca pue', 2000);
INSERT INTO Spectacle(noSpec, nomSpec, prixBaseSpec) VALUES (9, 'Je suis maitrise 7 sur Yasuo et Yi', 0);
---------------------- REPRESENTATION // need spectacle
INSERT INTO Representation(noRep, noSpec, dateRep, promoRep) VALUES (1, 1, '30/11/2021 10:00', 1);
INSERT INTO Representation(noRep, noSpec, dateRep, promoRep) VALUES (2, 1, '30/11/2021 16:00', 0.5);
INSERT INTO Representation(noRep, noSpec, dateRep, promoRep) VALUES (3, 2, '30/11/2021 18:00', 1);
INSERT INTO Representation(noRep, noSpec, dateRep, promoRep) VALUES (4, 1, '1/12/2021 10:00', 1);
---------------------- CATEGORIE
INSERT INTO Categorie(catZone, tauxZone) VALUES ('orchestre', 0.5);
INSERT INTO Categorie(catZone, tauxZone) VALUES ('balcon', 1);
INSERT INTO Categorie(catZone, tauxZone) VALUES ('poulailler', 0);
---------------------- ZONE // need categorie
INSERT INTO Zone(catZone) VALUES ('orchestre');
INSERT INTO Zone(catZone) VALUES ('balcon');
INSERT INTO Zone(catZone) VALUES ('poulailler');
---------------------- PLACE // need zone
INSERT INTO Place (noRang, noPlace, noZone) VALUES (1, 1, 1);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (1, 2, 1);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (1, 3, 1);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (1, 4, 1);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (2, 1, 2);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (2, 2, 2);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (2, 3, 2);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (2, 4, 2);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (3, 1, 3);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (3, 2, 3);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (3, 3, 3);
INSERT INTO Place (noRang, noPlace, noZone) VALUES (3, 4, 3);
---------------------- REDUCTION
-- INSERT INTO Reduction();
---------------------- VENTE // need reduction
-- INSERT INTO Vente();
---------------------- TICKET // need vente + place + representation
-- INSERT INTO Ticket();

