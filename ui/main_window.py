# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Esteban\Desktop\Code\WorkoutViewer\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lastDateInput = QtWidgets.QDateEdit(self.groupBox)
        self.lastDateInput.setReadOnly(True)
        self.lastDateInput.setObjectName("lastDateInput")
        self.horizontalLayout_4.addWidget(self.lastDateInput)
        self.importCSVButton = QtWidgets.QPushButton(self.groupBox)
        self.importCSVButton.setObjectName("importCSVButton")
        self.horizontalLayout_4.addWidget(self.importCSVButton)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.startEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.startEdit.setObjectName("startEdit")
        self.horizontalLayout_5.addWidget(self.startEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.endEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.endEdit.setObjectName("endEdit")
        self.horizontalLayout_5.addWidget(self.endEdit)
        self.validateButton = QtWidgets.QPushButton(self.groupBox_2)
        self.validateButton.setCheckable(False)
        self.validateButton.setObjectName("validateButton")
        self.horizontalLayout_5.addWidget(self.validateButton)
        self.resetButton = QtWidgets.QPushButton(self.groupBox_2)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_5.addWidget(self.resetButton)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.totalSessionsInput = QtWidgets.QSpinBox(self.groupBox_3)
        self.totalSessionsInput.setReadOnly(True)
        self.totalSessionsInput.setObjectName("totalSessionsInput")
        self.horizontalLayout_6.addWidget(self.totalSessionsInput)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.totalDaysSpin = QtWidgets.QSpinBox(self.groupBox_3)
        self.totalDaysSpin.setReadOnly(True)
        self.totalDaysSpin.setObjectName("totalDaysSpin")
        self.horizontalLayout_6.addWidget(self.totalDaysSpin)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.averageWorkoutsPerWeek = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.averageWorkoutsPerWeek.setObjectName("averageWorkoutsPerWeek")
        self.horizontalLayout_6.addWidget(self.averageWorkoutsPerWeek)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.lundi = QtWidgets.QSpinBox(self.groupBox_3)
        self.lundi.setObjectName("lundi")
        self.horizontalLayout_7.addWidget(self.lundi)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.mardi = QtWidgets.QSpinBox(self.groupBox_3)
        self.mardi.setObjectName("mardi")
        self.horizontalLayout_7.addWidget(self.mardi)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.mercredi = QtWidgets.QSpinBox(self.groupBox_3)
        self.mercredi.setObjectName("mercredi")
        self.horizontalLayout_7.addWidget(self.mercredi)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.jeudi = QtWidgets.QSpinBox(self.groupBox_3)
        self.jeudi.setObjectName("jeudi")
        self.horizontalLayout_7.addWidget(self.jeudi)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.vendredi = QtWidgets.QSpinBox(self.groupBox_3)
        self.vendredi.setObjectName("vendredi")
        self.horizontalLayout_7.addWidget(self.vendredi)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.samedi = QtWidgets.QSpinBox(self.groupBox_3)
        self.samedi.setObjectName("samedi")
        self.horizontalLayout_7.addWidget(self.samedi)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.dimanche = QtWidgets.QSpinBox(self.groupBox_3)
        self.dimanche.setObjectName("dimanche")
        self.horizontalLayout_7.addWidget(self.dimanche)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.allSessionsLayout = QtWidgets.QVBoxLayout()
        self.allSessionsLayout.setObjectName("allSessionsLayout")
        self.horizontalLayout.addLayout(self.allSessionsLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layout = QtWidgets.QVBoxLayout(self.tab_2)
        self.layout.setObjectName("layout")
        self.exoSelect = QtWidgets.QComboBox(self.tab_2)
        self.exoSelect.setObjectName("exoSelect")
        self.layout.addWidget(self.exoSelect)
        self.graphsLayout = QtWidgets.QVBoxLayout()
        self.graphsLayout.setObjectName("graphsLayout")
        self.layout.addLayout(self.graphsLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workout Viewer"))
        self.groupBox.setTitle(_translate("MainWindow", "Importer"))
        self.label.setText(_translate("MainWindow", "Date du dernier fichier chargé"))
        self.importCSVButton.setText(_translate("MainWindow", "Importer un fichier CSV"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filtrer"))
        self.label_2.setText(_translate("MainWindow", "Date de début"))
        self.label_3.setText(_translate("MainWindow", "Date de fin"))
        self.validateButton.setText(_translate("MainWindow", "Valider"))
        self.resetButton.setText(_translate("MainWindow", "Réinitialiser"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Séances"))
        self.label_4.setText(_translate("MainWindow", "Nombre de séances total"))
        self.label_12.setText(_translate("MainWindow", "Nombre de jours total"))
        self.label_13.setText(_translate("MainWindow", "Séances par semaine (moyenne)"))
        self.label_11.setText(_translate("MainWindow", "Lundi"))
        self.label_10.setText(_translate("MainWindow", "Mardi"))
        self.label_9.setText(_translate("MainWindow", "Mercredi"))
        self.label_8.setText(_translate("MainWindow", "Jeudi"))
        self.label_7.setText(_translate("MainWindow", "Vendredi"))
        self.label_6.setText(_translate("MainWindow", "Samedi"))
        self.label_5.setText(_translate("MainWindow", "Dimanche"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Accueil"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Graphiques"))
