import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic


req = """WITH tickets AS (
    SELECT noTicket, noRep
        FROM Ticket
            LEFT JOIN Vente USING(noAchat)
)
SELECT noRep, dateRep, promoRep, COUNT(noTicket) AS nbPlacesReservees, prixBaseSpec
    FROM Representation
        LEFT JOIN tickets USING(noRep)
        JOIN Spectacle USING(noSpec)
    WHERE nomSpec = ?
    GROUP BY noRep, dateRep, promoRep"""


class AppAddFct2(QDialog):
    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/add_fct_2.ui", self)
        self.data = data

        self.ui.comboBox_spec.currentTextChanged.connect(self.refreshResult)

        self.refreshCatList()

    # Fonction de mise à jour des spectacles
    @pyqtSlot()
    def refreshCatList(self):
        try:
            result = self.data.cursor().execute("SELECT DISTINCT nomSpec FROM Spectacle")

        except Exception as e:
            self.ui.comboBox_spec.setEnabled(False)

        else:
            self.ui.comboBox_spec.setEnabled(True)

            display.refreshGenericCombo(self.ui.comboBox_spec, result)

            self.ui.comboBox_spec.insertItem(0, "Sélectionner un spectacle")
            self.ui.comboBox_spec.setCurrentIndex(0)

            if len(self.ui.comboBox_spec.currentText()) > 0:
                self.refreshResult()

    # Fonction de mise à jour des catégories
    @pyqtSlot()
    def refreshResult(self):
        val = self.ui.comboBox_spec.currentText()

        display.refreshLabel(self.ui.prixBaseSpec, '0 €')

        if not val or val == "Sélectionner un spectacle":
            self.ui.tableSpecRep.setRowCount(0)
            
        else:
            try:
                result = self.data.cursor().execute(req, [val])
                
            except Exception as e:
                self.ui.tableSpecRep.setRowCount(0)
            
            else:
                firstRow = result.fetchone()

                if firstRow:
                    price = str(firstRow[4]) + ' €'
                    display.refreshLabel(self.ui.prixBaseSpec, price)

                display.refreshGenericData(self.ui.tableSpecRep, result)