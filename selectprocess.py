# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectprocess.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(443, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.processtable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processtable.sizePolicy().hasHeightForWidth())
        self.processtable.setSizePolicy(sizePolicy)
        self.processtable.setAutoFillBackground(False)
        self.processtable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.processtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.processtable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.processtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.processtable.setObjectName("processtable")
        self.processtable.setColumnCount(3)
        self.processtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.processtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.processtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.processtable.setHorizontalHeaderItem(2, item)
        self.processtable.horizontalHeader().setDefaultSectionSize(70)
        self.processtable.horizontalHeader().setStretchLastSection(True)
        self.processtable.verticalHeader().setVisible(False)
        self.processtable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.processtable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_2.addWidget(self.pushButton_Open)
        self.pushButton_Close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_2.addWidget(self.pushButton_Close)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton_CreateProcess = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CreateProcess.setObjectName("pushButton_CreateProcess")
        self.verticalLayout.addWidget(self.pushButton_CreateProcess)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Name of the Process:"))
        self.processtable.setSortingEnabled(True)
        item = self.processtable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.processtable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.processtable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Process Name"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_Close.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_CreateProcess.setText(_translate("MainWindow", "Create Process"))

