
import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

# Classe permettant d'afficher la fenêtre de visualisation des données
class AppTablesDataV1(QDialog):

    # Constructeur
    def __init__(self, data:sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/v1_tablesData.ui", self)
        self.data = data

        # On met à jour l'affichage avec les données actuellement présentes dans la base
        self.refreshAllTablesV1()

    ####################################################################################################################
    # Méthodes permettant de rafraichir les différentes tables
    ####################################################################################################################

    # Fonction de mise à jour de l'affichage d'une seule table
    def refreshTable(self, label, table, query):
        display.refreshLabel(label, "")
        try:
            cursor = self.data.cursor()
            result = cursor.execute(query)
        except Exception as e:
            table.setRowCount(0)
            display.refreshLabel(label, "Impossible d'afficher les données de la table : " + repr(e))
        else:
            display.refreshGenericData(table, result)


    # Fonction permettant de mettre à jour toutes les tables
    @pyqtSlot()
    def refreshAllTablesV1(self):
        self.refreshTable(self.ui.label_spectacle, self.ui.tableSpectacle,
            "SELECT noSpec, nomSpec, prixBaseSpec FROM Spectacle")

        self.refreshTable(self.ui.label_representation, self.ui.tableRepresentation,
            "SELECT noRep, noSpec, dateRep, promoRep FROM Representation")

        self.refreshTable(self.ui.label_categorie, self.ui.tableCategorie,
            "SELECT catZone, tauxZone FROM Categorie")

        self.refreshTable(self.ui.label_zone, self.ui.tableZone,
            "SELECT noZone, catZone FROM Zone")

        self.refreshTable(self.ui.label_place, self.ui.tablePlace,
            "SELECT noRang, noPlace, noZone FROM Place")

        self.refreshTable(self.ui.label_reduction, self.ui.tableReduction,
            "SELECT typeReduc, tauxReduc FROM Reduction")

        self.refreshTable(self.ui.label_ticket, self.ui.tableTicket,
            "SELECT noTicket, noAchat, noRep, noRang, noPlace, prixTotal, typeReduc FROM Ticket")

        self.refreshTable(self.ui.label_vente, self.ui.tableVente,
            "SELECT noAchat, dateAchat FROM Vente")
            
        self.refreshTable(self.ui.label_lesrepresentations, self.ui.tableLesRepresentations,
            "SELECT nomSpec, noRep, dateRep, nbPlacesDisponibles, nbPlacesOccupees FROM LesRepresentations")

        self.refreshTable(self.ui.label_lesventes, self.ui.tableLesVentes,
            "SELECT noAchat, montantTotal FROM LesVentes")