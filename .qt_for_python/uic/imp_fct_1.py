# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\uga\projectCEBD-2021\gui\imp_fct_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gererRep(object):
    def setupUi(self, gererRep):
        gererRep.setObjectName("gererRep")
        gererRep.resize(701, 399)
        self.verticalLayoutWidget = QtWidgets.QWidget(gererRep)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(11, 65, 341, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableRep = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableRep.setObjectName("tableRep")
        self.tableRep.setColumnCount(5)
        self.tableRep.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRep.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRep.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRep.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRep.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRep.setHorizontalHeaderItem(4, item)
        self.tableRep.horizontalHeader().setDefaultSectionSize(60)
        self.tableRep.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableRep)
        self.comboBox_spectacle = QtWidgets.QComboBox(gererRep)
        self.comboBox_spectacle.setGeometry(QtCore.QRect(11, 15, 341, 31))
        self.comboBox_spectacle.setObjectName("comboBox_spectacle")
        self.comboBox_spectacle.addItem("")
        self.tabActions = QtWidgets.QTabWidget(gererRep)
        self.tabActions.setGeometry(QtCore.QRect(360, 10, 331, 381))
        self.tabActions.setObjectName("tabActions")
        self.tabAjout = QtWidgets.QWidget()
        self.tabAjout.setObjectName("tabAjout")
        self.addSpec = QtWidgets.QPushButton(self.tabAjout)
        self.addSpec.setGeometry(QtCore.QRect(219, 155, 93, 28))
        self.addSpec.setObjectName("addSpec")
        self.label_dateRep = QtWidgets.QLabel(self.tabAjout)
        self.label_dateRep.setGeometry(QtCore.QRect(66, 280, 101, 31))
        self.label_dateRep.setObjectName("label_dateRep")
        self.addRep = QtWidgets.QPushButton(self.tabAjout)
        self.addRep.setEnabled(False)
        self.addRep.setGeometry(QtCore.QRect(220, 320, 93, 28))
        self.addRep.setObjectName("addRep")
        self.label_representation = QtWidgets.QLabel(self.tabAjout)
        self.label_representation.setGeometry(QtCore.QRect(20, 187, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.label_representation.setFont(font)
        self.label_representation.setObjectName("label_representation")
        self.doubleSpinBox_prixSpec = QtWidgets.QDoubleSpinBox(self.tabAjout)
        self.doubleSpinBox_prixSpec.setGeometry(QtCore.QRect(220, 117, 91, 22))
        self.doubleSpinBox_prixSpec.setObjectName("doubleSpinBox_prixSpec")
        self.lineEdit_nomSpec = QtWidgets.QLineEdit(self.tabAjout)
        self.lineEdit_nomSpec.setGeometry(QtCore.QRect(120, 77, 191, 22))
        self.lineEdit_nomSpec.setObjectName("lineEdit_nomSpec")
        self.label_spectacle = QtWidgets.QLabel(self.tabAjout)
        self.label_spectacle.setGeometry(QtCore.QRect(20, 17, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.label_spectacle.setFont(font)
        self.label_spectacle.setObjectName("label_spectacle")
        self.label_prixSpec = QtWidgets.QLabel(self.tabAjout)
        self.label_prixSpec.setGeometry(QtCore.QRect(55, 117, 55, 16))
        self.label_prixSpec.setObjectName("label_prixSpec")
        self.dateTimeEdit_dateRep = QtWidgets.QDateTimeEdit(self.tabAjout)
        self.dateTimeEdit_dateRep.setGeometry(QtCore.QRect(170, 280, 141, 31))
        self.dateTimeEdit_dateRep.setObjectName("dateTimeEdit_dateRep")
        self.label_nomSpec = QtWidgets.QLabel(self.tabAjout)
        self.label_nomSpec.setGeometry(QtCore.QRect(55, 77, 55, 21))
        self.label_nomSpec.setObjectName("label_nomSpec")
        self.label_promoRep = QtWidgets.QLabel(self.tabAjout)
        self.label_promoRep.setGeometry(QtCore.QRect(66, 240, 101, 31))
        self.label_promoRep.setObjectName("label_promoRep")
        self.label_specAddResult = QtWidgets.QLabel(self.tabAjout)
        self.label_specAddResult.setGeometry(QtCore.QRect(10, 160, 201, 21))
        self.label_specAddResult.setText("")
        self.label_specAddResult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_specAddResult.setObjectName("label_specAddResult")
        self.label_resAddResult = QtWidgets.QLabel(self.tabAjout)
        self.label_resAddResult.setGeometry(QtCore.QRect(0, 320, 221, 21))
        self.label_resAddResult.setText("")
        self.label_resAddResult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resAddResult.setObjectName("label_resAddResult")
        self.doubleSpinBox_promoRep = QtWidgets.QSpinBox(self.tabAjout)
        self.doubleSpinBox_promoRep.setGeometry(QtCore.QRect(230, 240, 81, 31))
        self.doubleSpinBox_promoRep.setObjectName("doubleSpinBox_promoRep")
        self.tabActions.addTab(self.tabAjout, "")
        self.tabSupp = QtWidgets.QWidget()
        self.tabSupp.setObjectName("tabSupp")
        self.label_representation_2 = QtWidgets.QLabel(self.tabSupp)
        self.label_representation_2.setGeometry(QtCore.QRect(20, 190, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.label_representation_2.setFont(font)
        self.label_representation_2.setObjectName("label_representation_2")
        self.label_spectacle_2 = QtWidgets.QLabel(self.tabSupp)
        self.label_spectacle_2.setGeometry(QtCore.QRect(20, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.label_spectacle_2.setFont(font)
        self.label_spectacle_2.setObjectName("label_spectacle_2")
        self.pushButton_supprSpec = QtWidgets.QPushButton(self.tabSupp)
        self.pushButton_supprSpec.setGeometry(QtCore.QRect(120, 100, 91, 31))
        self.pushButton_supprSpec.setObjectName("pushButton_supprSpec")
        self.pushButton_supprRep = QtWidgets.QPushButton(self.tabSupp)
        self.pushButton_supprRep.setGeometry(QtCore.QRect(200, 260, 91, 31))
        self.pushButton_supprRep.setObjectName("pushButton_supprRep")
        self.comboBox_supprRep = QtWidgets.QComboBox(self.tabSupp)
        self.comboBox_supprRep.setGeometry(QtCore.QRect(20, 260, 171, 31))
        self.comboBox_supprRep.setObjectName("comboBox_supprRep")
        self.comboBox_supprRep.addItem("")
        self.label_specDel = QtWidgets.QLabel(self.tabSupp)
        self.label_specDel.setGeometry(QtCore.QRect(4, 65, 321, 21))
        self.label_specDel.setText("")
        self.label_specDel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_specDel.setObjectName("label_specDel")
        self.label_specDelResult = QtWidgets.QLabel(self.tabSupp)
        self.label_specDelResult.setGeometry(QtCore.QRect(-4, 150, 331, 20))
        self.label_specDelResult.setText("")
        self.label_specDelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_specDelResult.setObjectName("label_specDelResult")
        self.label_resDelResult = QtWidgets.QLabel(self.tabSupp)
        self.label_resDelResult.setGeometry(QtCore.QRect(-3, 318, 331, 20))
        self.label_resDelResult.setText("")
        self.label_resDelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.label_resDelResult.setObjectName("label_resDelResult")
        self.tabActions.addTab(self.tabSupp, "")

        self.retranslateUi(gererRep)
        self.tabActions.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gererRep)

    def retranslateUi(self, gererRep):
        _translate = QtCore.QCoreApplication.translate
        gererRep.setWindowTitle(_translate("gererRep", "Gérer les représentations"))
        item = self.tableRep.horizontalHeaderItem(0)
        item.setText(_translate("gererRep", "noRep"))
        item = self.tableRep.horizontalHeaderItem(1)
        item.setText(_translate("gererRep", "date"))
        item = self.tableRep.horizontalHeaderItem(2)
        item.setText(_translate("gererRep", "promo"))
        item = self.tableRep.horizontalHeaderItem(3)
        item.setText(_translate("gererRep", "dispo"))
        item = self.tableRep.horizontalHeaderItem(4)
        item.setText(_translate("gererRep", "prises"))
        self.comboBox_spectacle.setItemText(0, _translate("gererRep", "Sélectionner un spectacle"))
        self.addSpec.setText(_translate("gererRep", "Créer"))
        self.label_dateRep.setText(_translate("gererRep", "Date / heure :"))
        self.addRep.setText(_translate("gererRep", "Créer"))
        self.label_representation.setText(_translate("gererRep", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Ajouter une représentation</span></p></body></html>"))
        self.label_spectacle.setText(_translate("gererRep", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Ajouter un spectacle</span></p></body></html>"))
        self.label_prixSpec.setText(_translate("gererRep", "Prix :"))
        self.label_nomSpec.setText(_translate("gererRep", "Nom :"))
        self.label_promoRep.setText(_translate("gererRep", "Promotion (%) :"))
        self.tabActions.setTabText(self.tabActions.indexOf(self.tabAjout), _translate("gererRep", "Ajout"))
        self.label_representation_2.setText(_translate("gererRep", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Supprimer une représentation</span></p></body></html>"))
        self.label_spectacle_2.setText(_translate("gererRep", "<html><head/><body><p><span style=\" font-size:12pt; text-decoration: underline;\">Supprimer ce spectacle</span></p></body></html>"))
        self.pushButton_supprSpec.setText(_translate("gererRep", "SUPPRIMER"))
        self.pushButton_supprRep.setText(_translate("gererRep", "SUPPRIMER"))
        self.comboBox_supprRep.setItemText(0, _translate("gererRep", "Choisir une représentation"))
        self.tabActions.setTabText(self.tabActions.indexOf(self.tabSupp), _translate("gererRep", "Suppression"))
