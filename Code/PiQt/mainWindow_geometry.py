# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Desktop/S4GRO-Cagius/Cagius/Code/PiQt/mainWindow_geometry.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 591, 103))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Fin = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.Fin.setObjectName("Fin")
        self.gridLayout_7.addWidget(self.Fin, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 1, 0, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 1, 2, 1, 1)
        self.Debut = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.Debut.setObjectName("Debut")
        self.gridLayout_7.addWidget(self.Debut, 2, 1, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Animal1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Animal1.setChecked(True)
        self.Animal1.setObjectName("Animal1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Animal1)
        self.horizontalLayout_2.addWidget(self.Animal1)
        self.Animal2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Animal2.setObjectName("Animal2")
        self.buttonGroup.addButton(self.Animal2)
        self.horizontalLayout_2.addWidget(self.Animal2)
        self.Animal3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Animal3.setObjectName("Animal3")
        self.buttonGroup.addButton(self.Animal3)
        self.horizontalLayout_2.addWidget(self.Animal3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 1, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 291, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Desactivation = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Desactivation.setObjectName("Desactivation")
        self.gridLayout_5.addWidget(self.Desactivation, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 3, 1, 1, 1)
        self.Activation = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.Activation.setObjectName("Activation")
        self.gridLayout_5.addWidget(self.Activation, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(310, 110, 289, 219))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem8, 3, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem9, 3, 0, 1, 1)
        self.Nettoyage = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.Nettoyage.setObjectName("Nettoyage")
        self.gridLayout_6.addWidget(self.Nettoyage, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 3, 1, 1, 1)
        self.Viderpoubelle = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.Viderpoubelle.setObjectName("Viderpoubelle")
        self.gridLayout_6.addWidget(self.Viderpoubelle, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 28))
        self.menubar.setObjectName("menubar")
        self.menuCagius = QtWidgets.QMenu(self.menubar)
        self.menuCagius.setObjectName("menuCagius")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCagius.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Nombre d\'animaux"))
        self.label_4.setText(_translate("MainWindow", "Heures d\'activités"))
        self.label_5.setText(_translate("MainWindow", "Début"))
        self.label_6.setText(_translate("MainWindow", "Fin"))
        self.Animal1.setText(_translate("MainWindow", "1"))
        self.Animal2.setText(_translate("MainWindow", "2"))
        self.Animal3.setText(_translate("MainWindow", "3"))
        self.Desactivation.setText(_translate("MainWindow", "Désactivation"))
        self.Activation.setText(_translate("MainWindow", "Activation"))
        self.label.setText(_translate("MainWindow", "Mode automatique de nettoyage"))
        self.label_2.setText(_translate("MainWindow", "Mode manuel"))
        self.Nettoyage.setText(_translate("MainWindow", "Nettoyage"))
        self.Viderpoubelle.setText(_translate("MainWindow", "Vider poubelle"))
        self.menuCagius.setTitle(_translate("MainWindow", "Cagius"))

