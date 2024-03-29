
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 1
class AppFctComp1Partie1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_1.ui", self)
        self.data = data
        self.ui.comboBox_categorie.currentTextChanged.connect(self.refreshResult)


    # Fonction de mise à joru de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        # TODO 1.1 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs prédéfinies dans l'interface une fois le fichier ui correspondant mis à jour
        display.refreshLabel(self.ui.label_fct_comp_1, "")

        val = self.ui.comboBox_categorie.currentText()

        if not val or val == "Choisir une catégorie":
            self.ui.table_fct_comp_1.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_1, "Veuillez indiquer un nom de catégorie")
        
        else:
            try:
                result = self.data.cursor().execute(
                    "SELECT noPlace, noRang, noZone FROM Place LEFT JOIN Zone USING(noZone) WHERE catZone = ? ORDER BY noRang, noPlace",
                    [val]
                )
                
            except Exception as e:
                self.ui.table_fct_comp_1.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_1, "Impossible d'afficher les résultats : " + repr(e))
            
            else:
                if display.refreshGenericData(self.ui.table_fct_comp_1, result) == 0:
                    display.refreshLabel(self.ui.label_fct_comp_1, "Aucun résultat")
