# Form implementation generated from reading ui file 'appGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 676)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 200, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 430, 561, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 40, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 80, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(430, 80, 61, 16))
        self.label_7.setObjectName("label_7")
        self.lineEditMu = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditMu.setGeometry(QtCore.QRect(90, 40, 101, 21))
        self.lineEditMu.setObjectName("lineEditMu")
        self.lineEditP = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditP.setGeometry(QtCore.QRect(290, 40, 101, 21))
        self.lineEditP.setObjectName("lineEditP")
        self.lineEditR0 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditR0.setGeometry(QtCore.QRect(490, 40, 101, 21))
        self.lineEditR0.setObjectName("lineEditR0")
        self.lineEditKb = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditKb.setGeometry(QtCore.QRect(290, 80, 101, 21))
        self.lineEditKb.setObjectName("lineEditKb")
        self.lineEditG = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditG.setGeometry(QtCore.QRect(490, 80, 101, 21))
        self.lineEditG.setObjectName("lineEditG")
        self.lineEditQ = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditQ.setGeometry(QtCore.QRect(90, 80, 101, 21))
        self.lineEditQ.setObjectName("lineEditQ")
        self.lineEditBD = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditBD.setGeometry(QtCore.QRect(320, 150, 71, 21))
        self.lineEditBD.setObjectName("lineEditBD")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 150, 81, 16))
        self.label_9.setObjectName("label_9")
        self.lineEditTT = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTT.setGeometry(QtCore.QRect(500, 150, 91, 21))
        self.lineEditTT.setObjectName("lineEditTT")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 150, 61, 16))
        self.label_11.setObjectName("label_11")
        self.lineEditTL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditTL.setGeometry(QtCore.QRect(100, 150, 91, 21))
        self.lineEditTL.setObjectName("lineEditTL")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 220, 61, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 190, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEditCL = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditCL.setGeometry(QtCore.QRect(100, 220, 91, 21))
        self.lineEditCL.setObjectName("lineEditCL")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 270, 561, 131))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("channel_flow.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application"))
        self.pushButton.setText(_translate("MainWindow", "RUN SCRIPT"))
        self.label.setText(_translate("MainWindow", "Fixed parameters for perfusion"))
        self.label_2.setText(_translate("MainWindow", "mu (Pa.s)"))
        self.label_3.setText(_translate("MainWindow", "p (kg/m3)"))
        self.label_4.setText(_translate("MainWindow", "r0 (m)"))
        self.label_5.setText(_translate("MainWindow", "K_b"))
        self.label_6.setText(_translate("MainWindow", "Q (m3/s)"))
        self.label_7.setText(_translate("MainWindow", "g (m/s2)"))
        self.lineEditMu.setText(_translate("MainWindow", "1.0016e-3"))
        self.lineEditP.setText(_translate("MainWindow", "1000"))
        self.lineEditR0.setText(_translate("MainWindow", "1.0e-4"))
        self.lineEditKb.setText(_translate("MainWindow", "0.265"))
        self.lineEditG.setText(_translate("MainWindow", "9.81"))
        self.lineEditQ.setText(_translate("MainWindow", "1.3888889e-12"))
        self.lineEditBD.setText(_translate("MainWindow", "25e-4"))
        self.label_8.setText(_translate("MainWindow", "Tunable parameters for perfusion"))
        self.label_9.setText(_translate("MainWindow", "bend diameter"))
        self.lineEditTT.setText(_translate("MainWindow", "60"))
        self.label_10.setText(_translate("MainWindow", "tube length"))
        self.label_11.setText(_translate("MainWindow", "tube turns"))
        self.lineEditTL.setText(_translate("MainWindow", "50e-2"))
        self.label_12.setText(_translate("MainWindow", "chip length"))
        self.label_13.setText(_translate("MainWindow", "Fixed parameters for chip"))
        self.lineEditCL.setText(_translate("MainWindow", "20e-2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
