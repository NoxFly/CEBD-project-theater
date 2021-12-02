import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


req = """SELECT noSpec, nomSpec, noRep, dateRep
    FROM LesRepresentations
    JOIN Spectacle USING(nomSpec)
    WHERE nbPlacesOccupees = 0"""

class AppAddFct1(QDialog):
    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/add_fct_1.ui", self)
        self.data = data

        self.refreshResult()

    # Fonction de mise à jour des catégories
    @pyqtSlot()
    def refreshResult(self):
        try:
            result = self.data.cursor().execute(req)
            
        except Exception as e:
            self.ui.tableListeRepresentations.setRowCount(0)
            display.refreshLabel(self.ui.label_rep_res, "Impossible d'afficher les résultats : " + repr(e))
        
        else:
            if display.refreshGenericData(self.ui.tableListeRepresentations, result) == 0:
                display.refreshLabel(self.ui.label_rep_res, "Aucun résultat")