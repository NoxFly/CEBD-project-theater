# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\codes\uga\projectCEBD-2021\gui\v1_tablesData.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tablesData(object):
    def setupUi(self, tablesData):
        tablesData.setObjectName("tablesData")
        tablesData.resize(1071, 599)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tablesData.sizePolicy().hasHeightForWidth())
        tablesData.setSizePolicy(sizePolicy)
        tablesData.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(tablesData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(tablesData)
        self.tabWidget.setObjectName("tabWidget")
        self.tabSpectacle = QtWidgets.QWidget()
        self.tabSpectacle.setObjectName("tabSpectacle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabSpectacle)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableSpectacle = QtWidgets.QTableWidget(self.tabSpectacle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableSpectacle.sizePolicy().hasHeightForWidth())
        self.tableSpectacle.setSizePolicy(sizePolicy)
        self.tableSpectacle.setMinimumSize(QtCore.QSize(0, 400))
        self.tableSpectacle.setMaximumSize(QtCore.QSize(1021, 16777215))
        self.tableSpectacle.setBaseSize(QtCore.QSize(0, 0))
        self.tableSpectacle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableSpectacle.setColumnCount(3)
        self.tableSpectacle.setObjectName("tableSpectacle")
        self.tableSpectacle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpectacle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpectacle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSpectacle.setHorizontalHeaderItem(2, item)
        self.tableSpectacle.horizontalHeader().setCascadingSectionResizes(True)
        self.tableSpectacle.horizontalHeader().setDefaultSectionSize(150)
        self.tableSpectacle.horizontalHeader().setHighlightSections(True)
        self.tableSpectacle.horizontalHeader().setMinimumSectionSize(50)
        self.tableSpectacle.horizontalHeader().setStretchLastSection(True)
        self.tableSpectacle.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableSpectacle)
        self.label_spectacle = QtWidgets.QLabel(self.tabSpectacle)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_spectacle.setPalette(palette)
        self.label_spectacle.setText("")
        self.label_spectacle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spectacle.setObjectName("label_spectacle")
        self.verticalLayout_2.addWidget(self.label_spectacle)
        self.tabWidget.addTab(self.tabSpectacle, "")
        self.tabRepresentation = QtWidgets.QWidget()
        self.tabRepresentation.setObjectName("tabRepresentation")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabRepresentation)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableRepresentation = QtWidgets.QTableWidget(self.tabRepresentation)
        self.tableRepresentation.setObjectName("tableRepresentation")
        self.tableRepresentation.setColumnCount(4)
        self.tableRepresentation.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableRepresentation.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRepresentation.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRepresentation.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableRepresentation.setHorizontalHeaderItem(3, item)
        self.tableRepresentation.horizontalHeader().setDefaultSectionSize(200)
        self.tableRepresentation.horizontalHeader().setMinimumSectionSize(50)
        self.tableRepresentation.horizontalHeader().setStretchLastSection(True)
        self.tableRepresentation.verticalHeader().setVisible(False)
        self.verticalLayout_5.addWidget(self.tableRepresentation)
        self.label_representation = QtWidgets.QLabel(self.tabRepresentation)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_representation.setPalette(palette)
        self.label_representation.setText("")
        self.label_representation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_representation.setObjectName("label_representation")
        self.verticalLayout_5.addWidget(self.label_representation)
        self.tabWidget.addTab(self.tabRepresentation, "")
        self.tabCategorie = QtWidgets.QWidget()
        self.tabCategorie.setObjectName("tabCategorie")
        self.tableCategorie = QtWidgets.QTableWidget(self.tabCategorie)
        self.tableCategorie.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tableCategorie.setObjectName("tableCategorie")
        self.tableCategorie.setColumnCount(2)
        self.tableCategorie.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableCategorie.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCategorie.setHorizontalHeaderItem(1, item)
        self.label_categorie = QtWidgets.QLabel(self.tabCategorie)
        self.label_categorie.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_categorie.setText("")
        self.label_categorie.setAlignment(QtCore.Qt.AlignCenter)
        self.label_categorie.setObjectName("label_categorie")
        self.tabWidget.addTab(self.tabCategorie, "")
        self.tabZone = QtWidgets.QWidget()
        self.tabZone.setObjectName("tabZone")
        self.tableZone = QtWidgets.QTableWidget(self.tabZone)
        self.tableZone.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tableZone.setObjectName("tableZone")
        self.tableZone.setColumnCount(2)
        self.tableZone.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(1, item)
        self.label_zone = QtWidgets.QLabel(self.tabZone)
        self.label_zone.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_zone.setText("")
        self.label_zone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_zone.setObjectName("label_zone")
        self.tabWidget.addTab(self.tabZone, "")
        self.tabPlace = QtWidgets.QWidget()
        self.tabPlace.setObjectName("tabPlace")
        self.tablePlace = QtWidgets.QTableWidget(self.tabPlace)
        self.tablePlace.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tablePlace.setObjectName("tablePlace")
        self.tablePlace.setColumnCount(3)
        self.tablePlace.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlace.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlace.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePlace.setHorizontalHeaderItem(2, item)
        self.label_place = QtWidgets.QLabel(self.tabPlace)
        self.label_place.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_place.setText("")
        self.label_place.setAlignment(QtCore.Qt.AlignCenter)
        self.label_place.setObjectName("label_place")
        self.tabWidget.addTab(self.tabPlace, "")
        self.tabReduction = QtWidgets.QWidget()
        self.tabReduction.setObjectName("tabReduction")
        self.tableReduction = QtWidgets.QTableWidget(self.tabReduction)
        self.tableReduction.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tableReduction.setObjectName("tableReduction")
        self.tableReduction.setColumnCount(2)
        self.tableReduction.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableReduction.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableReduction.setHorizontalHeaderItem(1, item)
        self.label_reduction = QtWidgets.QLabel(self.tabReduction)
        self.label_reduction.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_reduction.setText("")
        self.label_reduction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_reduction.setObjectName("label_reduction")
        self.tabWidget.addTab(self.tabReduction, "")
        self.tabTicket = QtWidgets.QWidget()
        self.tabTicket.setObjectName("tabTicket")
        self.tableTicket = QtWidgets.QTableWidget(self.tabTicket)
        self.tableTicket.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tableTicket.setObjectName("tableTicket")
        self.tableTicket.setColumnCount(5)
        self.tableTicket.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTicket.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTicket.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTicket.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTicket.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTicket.setHorizontalHeaderItem(4, item)
        self.label_ticket = QtWidgets.QLabel(self.tabTicket)
        self.label_ticket.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_ticket.setText("")
        self.label_ticket.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ticket.setObjectName("label_ticket")
        self.tabWidget.addTab(self.tabTicket, "")
        self.tabVente = QtWidgets.QWidget()
        self.tabVente.setObjectName("tabVente")
        self.tableVente = QtWidgets.QTableWidget(self.tabVente)
        self.tableVente.setGeometry(QtCore.QRect(11, 11, 1021, 466))
        self.tableVente.setObjectName("tableVente")
        self.tableVente.setColumnCount(4)
        self.tableVente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableVente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVente.setHorizontalHeaderItem(3, item)
        self.label_vente = QtWidgets.QLabel(self.tabVente)
        self.label_vente.setGeometry(QtCore.QRect(11, 484, 1021, 16))
        self.label_vente.setText("")
        self.label_vente.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vente.setObjectName("label_vente")
        self.tabWidget.addTab(self.tabVente, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(tablesData)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(tablesData)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(tablesData.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(tablesData)

    def retranslateUi(self, tablesData):
        _translate = QtCore.QCoreApplication.translate
        tablesData.setWindowTitle(_translate("tablesData", "BD Théâtre (V1)"))
        item = self.tableSpectacle.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noSpec"))
        item = self.tableSpectacle.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "nomSpec"))
        item = self.tableSpectacle.horizontalHeaderItem(2)
        item.setText(_translate("tablesData", "prixBaseSpec"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSpectacle), _translate("tablesData", "Spectacle"))
        item = self.tableRepresentation.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noRep"))
        item = self.tableRepresentation.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "noSpec"))
        item = self.tableRepresentation.horizontalHeaderItem(2)
        item.setText(_translate("tablesData", "dateRep"))
        item = self.tableRepresentation.horizontalHeaderItem(3)
        item.setText(_translate("tablesData", "promoRep"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRepresentation), _translate("tablesData", "Representation"))
        item = self.tableCategorie.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "catZone"))
        item = self.tableCategorie.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "tauxZone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCategorie), _translate("tablesData", "Categorie"))
        item = self.tableZone.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noZone"))
        item = self.tableZone.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "catZone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabZone), _translate("tablesData", "Zone"))
        item = self.tablePlace.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noRang"))
        item = self.tablePlace.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "noPlace"))
        item = self.tablePlace.horizontalHeaderItem(2)
        item.setText(_translate("tablesData", "noZone"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlace), _translate("tablesData", "Place"))
        item = self.tableReduction.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "typeReduc"))
        item = self.tableReduction.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "tauxReduc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabReduction), _translate("tablesData", "Reduction"))
        item = self.tableTicket.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noTicket"))
        item = self.tableTicket.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "noAchat"))
        item = self.tableTicket.horizontalHeaderItem(2)
        item.setText(_translate("tablesData", "noRep"))
        item = self.tableTicket.horizontalHeaderItem(3)
        item.setText(_translate("tablesData", "noRang"))
        item = self.tableTicket.horizontalHeaderItem(4)
        item.setText(_translate("tablesData", "noPlace"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTicket), _translate("tablesData", "Ticket"))
        item = self.tableVente.horizontalHeaderItem(0)
        item.setText(_translate("tablesData", "noAchat"))
        item = self.tableVente.horizontalHeaderItem(1)
        item.setText(_translate("tablesData", "dateAchat"))
        item = self.tableVente.horizontalHeaderItem(2)
        item.setText(_translate("tablesData", "prixGlobal"))
        item = self.tableVente.horizontalHeaderItem(3)
        item.setText(_translate("tablesData", "typeReduc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVente), _translate("tablesData", "Vente"))
        self.pushButton.setText(_translate("tablesData", "Fermer"))