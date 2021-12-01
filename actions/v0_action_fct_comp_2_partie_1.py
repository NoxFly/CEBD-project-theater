
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fonction à compléter 2
class AppFctComp2Partie1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/fct_comp_2.ui", self)
        self.data = data
        self.ui.comboBox_categorie.currentTextChanged.connect(self.refreshResult)
        self.refreshCatList()

    # Fonction de mise à jour des catégories
    @pyqtSlot()
    def refreshCatList(self):
        try:
            result = self.data.cursor().execute("SELECT DISTINCT catZone FROM Zone")

        except Exception as e:
            self.ui.comboBox_categorie.setEnabled(False)

        else:
            self.ui.comboBox_categorie.setEnabled(True)

            display.refreshGenericCombo(self.ui.comboBox_categorie, result)

            self.ui.comboBox_categorie.insertItem(0, "Choisir une catégorie")
            self.ui.comboBox_categorie.setCurrentIndex(0)

            if len(self.ui.comboBox_categorie.currentText()) > 0:
                self.refreshResult()

    # Fonction de mise à jour de l'affichage
    @pyqtSlot()
    def refreshResult(self):
        # TODO 1.2 : fonction à modifier pour remplacer la zone de saisie par une liste de valeurs issues de la BD une fois le fichier ui correspondant mis à jour
        display.refreshLabel(self.ui.label_fct_comp_2, "")

        val = self.ui.comboBox_categorie.currentText()

        if not val or val == "Choisir une catégorie":
            self.ui.table_fct_comp_2.setRowCount(0)
            display.refreshLabel(self.ui.label_fct_comp_2, "Veuillez indiquer un nom de catégorie")
        
        else:
            try:
                result = self.data.cursor().execute(
                    "SELECT noPlace, noRang, noZone FROM Place LEFT JOIN Zone USING(noZone) WHERE catZone = ? ORDER BY noRang, noPlace",
                    [val]
                )
                
            except Exception as e:
                self.ui.table_fct_comp_2.setRowCount(0)
                display.refreshLabel(self.ui.label_fct_comp_2, "Impossible d'afficher les résultats : " + repr(e))
            
            else:
                if display.refreshGenericData(self.ui.table_fct_comp_2, result) == 0:
                    display.refreshLabel(self.ui.label_fct_comp_2, "Aucun résultat")