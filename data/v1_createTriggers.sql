-- TODO 3.3 : Ajouter les éléments nécessaires pour créer le trigger (attention, syntaxe SQLite différent qu'Oracle)

-- NOTE : suite au probleme lie aux triggers, j'ai fait ce qu'a indique monsieur Mario dans son mail.
-- le delimiteur est le $

CREATE TRIGGER IF NOT EXISTS trigger_repCreation
    BEFORE INSERT
        ON Representation
        WHEN NEW.dateRep <= STRFTIME('%d/%m/%Y %H:%M', DATETIME('now'))
    BEGIN
        SELECT RAISE(ABORT, 'Cannot create a representation on a past time');
    END$

-- NOTE : ne permet pas d'importer les ventes / tickets de V0 qui sont deja passes depuis 2 ans
-- Ce trigger est cependant utile pour la partie 3.2
CREATE TRIGGER IF NOT EXISTS trigger_venteCreation
    BEFORE INSERT
        ON Vente
        WHEN NEW.noRep NOT IN (SELECT noRep FROM Representation WHERE noRep = NEW.noRep AND NEW.dateAchat < dateRep)
    BEGIN
        SELECT RAISE(ABORT, 'Cannot create a selling on a past representation');
    END$