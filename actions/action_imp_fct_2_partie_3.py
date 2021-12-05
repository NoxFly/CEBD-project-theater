
import sqlite3
from sqlite3.dbapi2 import Cursor
from utils import display
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QTableWidgetItem
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

class AppImpFct2(QDialog):
    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/imp_fct_2.ui", self)
        self.data = data

        # extra
        self.reductions = {}
        self.zones = {}
        self.currentRep = None
        self.saleState = False # some tickets are pending
        self.freePlaces = []


        self.updateComboReduc()
        self.zones = self.updateComboZone(True)
        self.updateComboSpec()

        # listeners
        self.ui.comboBox_spectacle.currentTextChanged.connect(self.onComboSpecChange)
        self.ui.comboBox_rep.currentTextChanged.connect(self.onComboRepChange)
        self.ui.tableTicketsRep.itemSelectionChanged.connect(self.onTicketSelection)
        # listeners to create ticket / update price dynamically
        self.ui.spinBox_nbTicket.valueChanged.connect(self.calculatePrice)
        self.ui.comboBox_typeReduc.currentTextChanged.connect(self.calculatePrice)
        self.ui.comboBox_zone.currentTextChanged.connect(self.onComboZoneChange)


        # push buttons
        self.ui.pushButton_deleteTicket.clicked.connect(self.onTicketDeletion)
        self.ui.pushButton_addTicket.clicked.connect(self.onTicketCommit)
        self.ui.buttonBox_confirmAction.rejected.connect(self.onTransactionCanceled)
        applyBtn = self.ui.buttonBox_confirmAction.button(QDialogButtonBox.Apply)
        applyBtn.clicked.connect(self.onTransactionConfirmed)





    ################# UPDATE COMBO BOXES / or tickets table #################

    def updateTicketsTable(self):
        selectedOption = self.ui.comboBox_rep.currentText()

        self.enableForm(False)
        self.ui.label_valeurPromoRep.setText('0')
        self.ui.label_formTicket.setText('')
        self.setTotalPrice(0)

        if not selectedOption or selectedOption == "Filtrer une date de représentation":
            self.enableActions(False)
            self.ui.tableTicketsRep.horizontalHeader().hide()
            self.currentRep = None
            self.greyText(self.ui.label_aucunSpec, 'Aucune représentation sélectionnée')
            self.freePlaces = []

        elif self.getCurrentRep():
            self.ui.label_valeurPromoRep.setText(str(int(self.currentRep['promoRep'] * 100)))
            
            if self.currentRep['nbPlacesDisponibles'] == 0:
                self.ui.label_formTicket.setText("Plus de place disponible")
                self.ui.pushButton_addTicket.setEnabled(False)
                self.enableForm(False)
            
            else:
                self.ui.pushButton_addTicket.setEnabled(True)
                self.enableForm(True)

            try:
                result = self.data.cursor().execute(
                    """SELECT noAchat, noTicket, noRang, noPlace, typeReduc, prixTotal
                        FROM Ticket
                        WHERE noRep = ?""", [self.currentRep['noRep']])

            except Exception as e:
                print("onComboRepChange error : ", e)

            else:
                self.freePlaces = self.getFreePlacesOfRep()

                if display.refreshGenericData(self.ui.tableTicketsRep, result) > 0:
                    self.ui.tableTicketsRep.horizontalHeader().show()
                    self.ui.label_aucunSpec.setText('')

                else:
                    self.greyText(self.ui.label_aucunSpec, 'Aucune réservation trouvée')
                    self.ui.tableTicketsRep.horizontalHeader().hide()

        self.updateComboZone()
        self.ui.spinBox_nbTicket.setMaximum(len(self.getFreePlacesOfZone()))

        self.onTransactionCanceled()
        self.calculatePrice()

    
    def updateComboSpec(self):
        self.ui.comboBox_spectacle.clear()

        try:
            result = self.data.cursor().execute("SELECT DISTINCT nomSpec FROM Spectacle")

        except Exception as e:
            print("Failed to recover spectacles :", e)

        else:
            display.refreshGenericCombo(self.ui.comboBox_spectacle, result)

        self.ui.comboBox_spectacle.insertItem(0, "Sélectionner un spectacle")
        self.ui.comboBox_spectacle.setCurrentIndex(0)

        if len(self.ui.comboBox_spectacle.currentText()) > 0:
            self.onComboSpecChange()

    def updateComboReduc(self):
        self.ui.comboBox_typeReduc.clear()
        self.reductions = {}

        try:
            result = self.data.cursor().execute("SELECT typeReduc, tauxReduc FROM Reduction")

        except Exception as e:
            print("updateComboReduc error : ", e)

        else:
            data = result.fetchall()

            for red in data:
                self.reductions[red[0]] = red[1]
                self.ui.comboBox_typeReduc.addItem(red[0])
            

    def updateComboZone(self, allZones:bool=False):
        self.ui.comboBox_zone.clear()

        try:
            result = None

            if allZones or not self.currentRep:
                result = self.data.cursor().execute("SELECT catZone, tauxZone, noZone FROM Categorie LEFT JOIN Zone USING(catZone)")
            else:
                result = self.getFreeZoneOfRep(self.currentRep['noRep'])

        except Exception as e:
            print("updateComboZone error : ", e)
            return {}

        else:
            if result:
                data = result.fetchall()
                returnedData = {}

                for z in data:
                    returnedData[z[0]] = { 'taux': z[1], 'no': z[2] }
                    self.ui.comboBox_zone.addItem(z[0])

                return returnedData
            
            return {}





    ################# HANDLERS #################

    def onComboSpecChange(self):
        selectedOption = self.ui.comboBox_spectacle.currentText()

        self.ui.comboBox_rep.clear()
        self.ui.tableTicketsRep.setRowCount(0)

        self.ui.comboBox_rep.insertItem(0, "Filtrer une date de représentation")
        self.ui.comboBox_rep.setCurrentIndex(0)

        if not selectedOption or selectedOption == "Sélectionner un spectacle":
            self.enableActions(False)
            self.enableForm(False)
            self.ui.comboBox_rep.setEnabled(False)
            self.ui.label_montant_spec.setText('0.0')
            self.greyText(self.ui.label_aucunSpec, 'Aucun spectacle sélectionné')

        else:
            self.ui.comboBox_rep.setEnabled(True)

            try:
                result = self.data.cursor().execute("SELECT dateRep FROM LesRepresentations WHERE nomSpec = ?", [selectedOption])
                result2 = self.data.cursor().execute("SELECT prixBaseSpec FROM Spectacle WHERE nomSpec = ?", [selectedOption])
            
            except Exception as e:
                print("onComboSpecChange error : ", e)
            
            else:
                result2 = result2.fetchone()

                if result2 and len(result2) > 0:
                    self.ui.label_montant_spec.setText(str(float(result2[0])))
                
                # not using refreshGenericCombo because it will handle
                # the onComboRepChange with new values while we don't want to
                datesRep = result.fetchall()

                for date in datesRep:
                    self.ui.comboBox_rep.addItem(date[0])

        self.freePlaces = []
        self.onTransactionCanceled()
        self.calculatePrice()
                

    def onComboRepChange(self):
        self.updateTicketsTable()

    
    def onComboZoneChange(self):
        # update nb tickets and all stuff
        self.freePlaces = self.getFreePlacesOfRep()
        self.ui.spinBox_nbTicket.setMaximum(len(self.getFreePlacesOfZone()))

        # update price
        self.calculatePrice()


    def onTicketSelection(self):
        self.ui.pushButton_deleteTicket.setEnabled(True)


    def onTicketDeletion(self):
        self.ui.pushButton_deleteTicket.setEnabled(False)

        rowNumber = self.ui.tableTicketsRep.currentRow()
        columnCount = self.ui.tableTicketsRep.columnCount()

        noTicket = None

        # recover the noTicket of the ticket to delete
        for i in range(columnCount):
            headerText = self.ui.tableTicketsRep.horizontalHeaderItem(i).text()

            if headerText == "noTicket":
                noTicket = self.ui.tableTicketsRep.item(rowNumber, i).text()

        # just to ensure
        if noTicket != None:
            try:
                self.data.cursor().execute("DELETE FROM Ticket WHERE noTicket = ?", [noTicket])

            except Exception as e:
                self.ui.label_feedback.setText("Une erreur est survenue")
                print("onTicketDeletion error : ", e)
            
            else:
                self.data.commit()

                self.ui.tableTicketsRep.removeRow(rowNumber)

                self.updateComboZone()
                self.enableForm(True)
                self.ui.pushButton_addTicket.setEnabled(True)
                self.ui.pushButton_deleteTicket.setEnabled(False)

                self.ui.label_feedback.setText("Ticket supprimé avec succès")


    def onTicketCommit(self):
        nbTicket = self.ui.spinBox_nbTicket.value()

        if nbTicket == 0:
            return

        #
        if not self.saleState:
            self.ui.tableTicketsToAdd.setRowCount(0)
            self.setTotalPrice(0)


        self.saleState = True

        montantTickets = float(self.ui.label_montantAvecReduc.text())
        prixParTicket = montantTickets / nbTicket

        zone = self.ui.comboBox_zone.currentText()

        # update total price
        self.setTotalPrice(self.getTotalPrice() + montantTickets)

        # update label (no tickets) + buttons
        self.ui.buttonBox_confirmAction.setEnabled(True)
        self.ui.tableTicketsToAdd.horizontalHeader().show()

        self.ui.label_aucunTicket.setText('')

        # update table
        rowN = self.ui.tableTicketsToAdd.rowCount()

        # get free places of selected zone
        places = self.getFreePlacesOfZone(self.zones[zone]['no'])

        # update remaining places in the form
        # and remove the zone from the comboBox in case there's no more available places
        # self.updateComboZone() can't be done here because nothing's done in the db
        newMax = self.ui.spinBox_nbTicket.maximum() - nbTicket
        tmpPlaces = None

        if newMax <= 0:
            self.ui.spinBox_nbTicket.setValue(1)
            self.ui.comboBox_zone.removeItem(self.ui.comboBox_zone.currentIndex())

            if self.ui.comboBox_zone.count() > 0:
                tmpPlaces = self.getFreePlacesOfZone()
                newMax = len(tmpPlaces)
            else:
                newMax = 0

        self.ui.spinBox_nbTicket.setMaximum(newMax)


        for i in range(nbTicket):
            self.ui.tableTicketsToAdd.insertRow(rowN)

            p = places.pop(0)
            (noPlace, noRang, noZone) = p

            self.freePlaces.remove(p)

            columns = (
                QTableWidgetItem(zone), # itemCatZone
                QTableWidgetItem(str(noRang)), # itemNoRang
                QTableWidgetItem(str(noPlace)), # itemNoPlace
                QTableWidgetItem(self.ui.comboBox_typeReduc.currentText()), # itemReductionType
                QTableWidgetItem(str(prixParTicket)) # itemPrix
            )

            for j in range(len(columns)):
                self.ui.tableTicketsToAdd.setItem(rowN, j, columns[j])

        if tmpPlaces != None:
            self.freePlaces = self.getFreePlacesOfRep()


    def onTransactionCanceled(self):
        self.saleState = False

        self.ui.buttonBox_confirmAction.setEnabled(False)
        self.ui.tableTicketsToAdd.horizontalHeader().hide()

        self.setTotalPrice(0)

        self.updateComboZone()

        newMax = len(self.getFreePlacesOfZone())
        self.ui.spinBox_nbTicket.setMaximum(newMax)

        if newMax > 0:
            self.ui.spinBox_nbTicket.setValue(1)

        self.ui.tableTicketsToAdd.setRowCount(0)
        self.greyText(self.ui.label_aucunTicket, 'Aucun ticket à afficher')


    def onTransactionConfirmed(self):
        try:
            self.ui.buttonBox_confirmAction.setEnabled(False)

            now = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm")
            
            self.data.cursor().execute("INSERT INTO Vente(dateAchat) VALUES(?)", [now])
            noAchat = self.data.cursor().execute("SELECT last_insert_rowid()").fetchone()[0]

            T = self.ui.tableTicketsToAdd

            header = []

            nRow = T.rowCount()
            nCol = T.columnCount()

            # adding tickets to db
            # step 2 : recovering the headers
            for i in range(nCol):
                header.append(T.horizontalHeaderItem(i).text())


            # step 3 : for each ticket
            for i in range(nRow):
                ticket = {}
                # step 3.1 : create ticket
                for j in range(nCol):
                    ticket[header[j]] = T.item(i, j).text()

                ticket = [
                    noAchat,
                    self.currentRep['noRep'],
                    int(ticket['noRang']),
                    int(ticket['noPlace']),
                    float(ticket['prix']),
                    ticket['reduction']
                ]

                # step 3.2 : db req
                self.data.cursor().execute(
                    """INSERT INTO Ticket(noAchat, noRep, noRang, noPlace, prixTotal, typeReduc)
                        VALUES(?, ?, ?, ?, ?, ?)""", ticket)


        except Exception as e:
            print("onTransactionConfirmed error : ", e)
            self.data.rollback()
            self.ui.label_feedback.setText("Une erreur est survenue")
            self.ui.buttonBox_confirmAction.setEnabled(True)

        else:
            self.data.commit()
            self.saleState = False
            self.ui.label_feedback.setText("Vente confirmée")
            self.updateTicketsTable()






    ################# EXTRA #################

    def getCurrentRep(self) -> bool:
        try:
            result = self.data.cursor().execute(
                """
                SELECT nomSpec, noRep, dateRep, promoRep, nbPlacesDisponibles, nbPlacesOccupees
                    FROM LesRepresentations
                    WHERE dateRep = ?""", [self.ui.comboBox_rep.currentText()])
        
        except Exception as e:
            print("getCurrentRep error : ", e)
            self.currentRep = None
            return False

        else:
            keys = ['nomSpec', 'noRep', 'dateRep', 'promoRep', 'nbPlacesDisponibles', 'nbPlacesOccupees']
            self.currentRep = {}
            data = result.fetchone()

            l = min(len(data), len(keys))

            for i in range(l):
                self.currentRep[keys[i]] = data[i]

            return True


    def getFreeZoneOfRep(self, noRep: int) -> Cursor:
        req = """WITH
            ZonesPleines AS (
                SELECT noPlace, noRang
                    FROM Ticket
                    WHERE noRep = ?
            ),
            NumeroZones AS (
                SELECT DISTINCT noZone
                    FROM Place
                    WHERE (noPlace, noRang) NOT IN ZonesPleines
            )
        SELECT catZone, tauxZone, noZone AS zones
            FROM Categorie
            LEFT JOIN Zone USING(catZone)
            WHERE noZone IN NumeroZones"""

        try:
            return self.data.cursor().execute(req, [noRep])

        except Exception as e:
            print("getFreeZoneOfRep error : ", e)
            return None

    def getFreePlacesOfRep(self, noRep: int=-1) -> list:
        req = """WITH PlacesPrises AS (
                    SELECT noPlace, noRang
                    FROM Ticket
                    WHERE noRep = ?
                )
                SELECT noPlace, noRang, noZone
                    FROM Place
                    WHERE (noPlace, noRang) NOT IN PlacesPrises"""

        try:
            if noRep == -1 and self.currentRep != None:
                noRep = self.currentRep['noRep']
            
            if noRep > -1:
                return self.data.cursor().execute(req, [noRep]).fetchall()
            
            return []

        except Exception as e:
            print("getFreePlacesOfRep error : ", e)
            return []


    def getFreePlacesOfZone(self, noZone:int=-1):
        currentZone = self.ui.comboBox_zone.currentText()
        
        if currentZone == '':
            return []
        
        if noZone == -1:
            noZone = self.zones[currentZone]['no']

        return [p for p in self.freePlaces if p[2] == noZone]


    def calculatePrice(self):
        nbTickets = self.ui.spinBox_nbTicket.value()
        typeReduc = self.ui.comboBox_typeReduc.currentText()
        zone = self.ui.comboBox_zone.currentText()

        label_prixTicket = self.ui.label_montant_ticket
        label_prixSansPromo = self.ui.label_montant
        label_prixAvecPromo = self.ui.label_montantAvecReduc

        prixSpec = float(self.ui.label_montant_spec.text())
        promoRep = 1 - (self.currentRep['promoRep'] if self.currentRep else 0) # 0 <= p <= 1
        valeurReduc = 1 - self.reductions[typeReduc] # 0 <= r <= 1
        valeurZone = 1 if zone == '' else self.zones[zone]['taux'] # 1 <= z <= 2

        prixTicket = prixSpec * valeurZone * valeurReduc
        prixSansPromo = prixTicket * nbTickets
        prixAvecPromo = (prixSansPromo * promoRep)

        label_prixTicket.setText(str(prixTicket))
        label_prixSansPromo.setText(str(prixSansPromo))
        label_prixAvecPromo.setText(str(prixAvecPromo))







    ################# EXTRA QT SHORTCUT FUNCTIONS #################

    def enableActions(self, enable: bool):
        self.ui.pushButton_addTicket.setEnabled(enable)
        self.ui.pushButton_deleteTicket.setEnabled(enable)
        self.ui.buttonBox_confirmAction.setEnabled(enable)

    def enableForm(self, enable: bool):
        self.ui.spinBox_nbTicket.setEnabled(enable)
        self.ui.comboBox_typeReduc.setEnabled(enable)
        self.ui.comboBox_zone.setEnabled(enable)


    def greyText(self, label, text: str):
        label.setText(text)
        label.setStyleSheet("color: #797979")

    def getTotalPrice(self) -> float:
        return float(self.ui.label_montantTotal.text())

    def setTotalPrice(self, amount):
        self.ui.label_montantTotal.setText(str(float(amount)))