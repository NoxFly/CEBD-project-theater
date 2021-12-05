

import sqlite3
from utils import display
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import QDateTime
from PyQt5 import uic

class AppImpFct1(QDialog):
    # Constructeur
    def __init__(self, data: sqlite3.Connection):
        super(QDialog, self).__init__()
        self.ui = uic.loadUi("gui/imp_fct_1.ui", self)
        self.data = data

        self.updateComboSpec()

        # listeners
        self.ui.comboBox_spectacle.currentTextChanged.connect(self.onComboSpecChange)

        # LEFT REP TABLE
        self.ui.tableRep.setColumnWidth(0, 55)
        self.ui.tableRep.setColumnWidth(1, 110)
        self.ui.tableRep.setColumnWidth(2, 50)
        self.ui.tableRep.horizontalHeader().setStretchLastSection(True)

        # SPEC PRICE - DOUBLE SPIN BOX
        self.ui.doubleSpinBox_prixSpec.setMinimum(0)
        self.ui.doubleSpinBox_prixSpec.setSingleStep(0.01)

        # REP PROMO - DOUBLE SPIN BOX
        self.ui.doubleSpinBox_promoRep.setMinimum(0)
        self.ui.doubleSpinBox_promoRep.setMaximum(100)
        self.ui.doubleSpinBox_promoRep.setSingleStep(1)

        # REP DATE TIME
        self.ui.dateTimeEdit_dateRep.setMinimumDateTime(QDateTime.currentDateTime())

        # PUSH BUTTONS
        self.ui.addSpec.clicked.connect(self.onSpecCreate)
        self.ui.addRep.clicked.connect(self.onRepCreate)

        self.ui.pushButton_supprSpec.clicked.connect(self.onSpecDeletion)
        self.ui.pushButton_supprRep.clicked.connect(self.onRepDeletion)


    # select spectacle
    
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

    def onComboSpecChange(self):
        selectedOption = self.ui.comboBox_spectacle.currentText()
        
        self.ui.comboBox_supprRep.clear()


        if not selectedOption or selectedOption == "Sélectionner un spectacle":
            self.ui.tableRep.setRowCount(0)
            self.ui.tabActions.setTabEnabled(1, False)
            self.ui.addSpec.setEnabled(False)
            self.ui.addRep.setEnabled(False)

        else:
            self.ui.tabActions.setTabEnabled(1, True)
            self.ui.addSpec.setEnabled(True)
            self.ui.addRep.setEnabled(True)

            # update the spec name in the deletion section
            self.ui.label_specDel.setText(f"Supprimer \"{selectedOption}\" ?")

            try:
                result = self.data.cursor().execute("SELECT noRep, dateRep, promoRep, nbPlacesDisponibles, nbPlacesOccupees FROM LesRepresentations WHERE nomSpec = ? ORDER BY noRep", [selectedOption])

            except Exception as e:
                print("Failed to recover representations :", e)

            else:
                # update comboBox for rep deletion
                res = result.fetchall()

                if res and len(res) > 0:
                    for row in res:
                        self.ui.comboBox_supprRep.addItem(row[1])

                display.refreshGenericData(self.ui.tableRep, res)


    # ajout
    def onRepCreate(self):
        self.ui.label_resAddResult.setText("")

        promoRep = self.ui.doubleSpinBox_promoRep.value() / 100
        dateRep = self.ui.dateTimeEdit_dateRep.dateTime().toString("dd/MM/yyyy hh:mm")

        noSpec = self.getCurrentSpecId()

        # first, verify that we'll not add a rep on the same date of existing one, for any spec
        # because there's only one room
        # /!\ IMPORTANT : we cannot use the WHERE clause, because SQLITE doesn't have a time comparison
        # (or it's too expensive to do)
        allDates = [row[0] for row in self.data.cursor().execute("SELECT dateRep FROM Representation").fetchall()]

        if noSpec:
            if dateRep not in allDates:
                try:
                    self.data.cursor().execute("INSERT INTO Representation(noSpec, dateRep, promoRep) VALUES(?, ?, ?)", [noSpec, dateRep, promoRep])
                    # retrieve the entiere inserted row so we also have its id
                    result = self.data.cursor().execute(
                        """SELECT noRep, dateRep, promoRep, nbPlacesDisponibles, nbPlacesOccupees
                            FROM LesRepresentations
                            WHERE nomSpec = ? AND dateRep = ?""",
                        [self.ui.comboBox_spectacle.currentText(), dateRep]
                    )
                    
                except Exception as e:
                    self.ui.label_resAddResult.setText("Une erreur est survenue")
                    print(e)
                    
                else:
                    self.data.commit()

                    rowPosition = self.tableRep.rowCount()
                    self.ui.tableRep.insertRow(rowPosition)

                    result = result.fetchone()

                    for i in range(len(result)):
                        self.ui.tableRep.setItem(rowPosition , i, QTableWidgetItem(str(result[i])))

                    self.ui.label_resAddResult.setText("Représentation créée")

            else:
                self.ui.label_resAddResult.setText("Une représentation a déjà lieu à cette date")

        else:
            self.ui.label_resAddResult.setText("Une erreur est survenue")


    def onSpecCreate(self):
        self.ui.label_specAddResult.setText("")

        specName = self.ui.lineEdit_nomSpec.text().strip()
        specPrice = self.ui.doubleSpinBox_prixSpec.value()

        if len(specName) > 0:
            allSpecs = [row[0] for row in self.data.cursor().execute("SELECT nomSpec FROM Spectacle").fetchall()]
            
            if specName not in allSpecs:
                try:
                    self.data.cursor().execute("INSERT INTO Spectacle(nomSpec, prixBaseSpec) VALUES (?, ?)", [specName, specPrice])

                except Exception as e:
                    self.ui.label_specAddResult.setText("Une erreur est survenue")

                else:
                    self.data.commit()
                    
                    self.ui.comboBox_spectacle.addItem(specName)
                    self.ui.label_specAddResult.setText("Spectacle créé avec succès")
                
            else:
                self.ui.label_specAddResult.setText("Ce spectacle existe déjà")

        else:
            self.ui.label_specAddResult.setText("Vous devez spécifier un nom de spectacle")


    # suppression

    def onSpecDeletion(self):
        if self.deleteAllRepFromCurrentSpec():
            specName = self.ui.comboBox_spectacle.currentText()

            try:
                self.data.cursor().execute("DELETE FROM Spectacle WHERE nomSpec = ?", [specName])

            except Exception as e:
                self.ui.label_specDelResult.setText("Une erreur est survenue")
                print(e)

            else:
                self.data.commit()

                i = self.ui.comboBox_spectacle.findText(specName)
                self.ui.comboBox_spectacle.removeItem(i)
                self.ui.comboBox_spectacle.setCurrentIndex(0)

                self.ui.label_specDelResult.setText("Spectacle supprimé avec succès")
        else:
            self.ui.label_specDelResult.setText("Une erreur est survenue")

    def onRepDeletion(self):
        dateRep = self.ui.comboBox_supprRep.currentText()

        noSpec = self.getCurrentSpecId()

        if noSpec:
            try:
                self.data.cursor().execute("DELETE FROM Representation WHERE noSpec = ? AND dateRep = ?", [noSpec, dateRep])

            except Exception as e:
                self.ui.label_resDelResult.setText("Une erreur est survenue")
                print(e)

            else:
                self.data.commit()

                # update comboBox
                i = self.ui.comboBox_supprRep.findText(dateRep)
                self.ui.comboBox_supprRep.removeItem(i)
                self.ui.comboBox_supprRep.setCurrentIndex(0)

                # update table
                for row in range(self.tableRep.rowCount()):
                    item = self.tableRep.item(row, 1)

                    if item.text() == dateRep:
                        self.ui.tableRep.removeRow(row)
                        break

                self.ui.label_resDelResult.setText("Représentation supprimée avec succès")
    

    ####
    def getCurrentSpecId(self):
        nomSpec = self.ui.comboBox_spectacle.currentText()

        try:
            result = self.data.cursor().execute("SELECT noSpec FROM Spectacle WHERE nomSpec = ?", [nomSpec])

        except Exception as e:
            return None

        else:
            res = result.fetchone()

            if res:
                return res[0]

        return None


    def deleteAllRepFromCurrentSpec(self):
        nRow = self.ui.tableRep.rowCount()

        if nRow > 0:
            noSpec = self.getCurrentSpecId()

            if noSpec:
                # then delete every rep that's linked to this id
                try:
                    self.data.cursor().execute("DELETE FROM Representation WHERE noSpec = ?", [noSpec])

                except Exception as e:
                    return False

                else:
                    self.data.commit()
                    return True

            else:
                return False

        return True