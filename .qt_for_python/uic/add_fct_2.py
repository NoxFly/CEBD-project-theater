# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\uga\projectCEBD-2021\gui\add_fct_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_specReserves(object):
    def setupUi(self, specReserves):
        specReserves.setObjectName("specReserves")
        specReserves.resize(577, 408)
        self.verticalLayoutWidget = QtWidgets.QWidget(specReserves)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 561, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableSpecRep = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableSpecRep.setObjectName("tableSpecRep")
        self.tableSpecRep.setColumnCount(4)
        self.tableSpecRep.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpecRep.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpecRep.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpecRep.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpecRep.setHorizontalHeaderItem(3, item)
        self.tableSpecRep.horizontalHeader().setDefaultSectionSize(139)
        self.tableSpecRep.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableSpecRep)
        self.comboBox_spec = QtWidgets.QComboBox(specReserves)
        self.comboBox_spec.setGeometry(QtCore.QRect(11, 10, 441, 31))
        self.comboBox_spec.setObjectName("comboBox_spec")
        self.comboBox_spec.addItem("")
        self.prixBaseSpec = QtWidgets.QLabel(specReserves)
        self.prixBaseSpec.setGeometry(QtCore.QRect(495, 16, 71, 21))
        self.prixBaseSpec.setScaledContents(False)
        self.prixBaseSpec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.prixBaseSpec.setObjectName("prixBaseSpec")
        self.label = QtWidgets.QLabel(specReserves)
        self.label.setGeometry(QtCore.QRect(482, 16, 55, 21))
        self.label.setObjectName("label")

        self.retranslateUi(specReserves)
        QtCore.QMetaObject.connectSlotsByName(specReserves)

    def retranslateUi(self, specReserves):
        _translate = QtCore.QCoreApplication.translate
        specReserves.setWindowTitle(_translate("specReserves", "Places des représentations de chaque spectacle"))
        item = self.tableSpecRep.horizontalHeaderItem(0)
        item.setText(_translate("specReserves", "noRep"))
        item = self.tableSpecRep.horizontalHeaderItem(1)
        item.setText(_translate("specReserves", "dateRep"))
        item = self.tableSpecRep.horizontalHeaderItem(2)
        item.setText(_translate("specReserves", "promoRep"))
        item = self.tableSpecRep.horizontalHeaderItem(3)
        item.setText(_translate("specReserves", "nbPlacesReservees"))
        self.comboBox_spec.setItemText(0, _translate("specReserves", "Sélectionner un spectacle"))
        self.prixBaseSpec.setText(_translate("specReserves", "0 €"))
        self.label.setText(_translate("specReserves", "Prix :"))
