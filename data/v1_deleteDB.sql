-- TODO 1.3 : Détruire les tables manquantes et modifier celles ci-dessous

-- dans l'ordre suivant les foreign key

-- les triggers
DROP TRIGGER IF EXISTS trigger_repCreation;
DROP TRIGGER IF EXISTS trigger_venteCreation;

-- d'abord les vues
DROP VIEW IF EXISTS LesRepresentations;
DROP VIEW IF EXISTS LesVentes;

-- ce qui a des foreign key
DROP TABLE IF EXISTS Ticket;

DROP TABLE IF EXISTS Place;
DROP TABLE IF EXISTS Zone;
DROP TABLE IF EXISTS Representation;

-- ce qui n'a aucune dependance mais dont
-- certaines entites dependent (et qui
-- donc viennent d'etre supprimees)
DROP TABLE IF EXISTS Categorie;
DROP TABLE IF EXISTS Reduction;
DROP TABLE IF EXISTS Spectacle;
DROP TABLE IF EXISTS Vente;