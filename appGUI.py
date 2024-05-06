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
        MainWindow.resize(623, 658)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 151, 661))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(131, 216, 243);\n"
"}\n"
"\n"
"QPushButton {\n"
"    text-align:left;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(255, 255, 255);\n"
"    font-weight:bold;\n"
"}")
        self.widget.setObjectName("widget")
        self.homeButton = QtWidgets.QPushButton(parent=self.widget)
        self.homeButton.setGeometry(QtCore.QRect(10, 50, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.homeButton.setFont(font)
        self.homeButton.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setIconSize(QtCore.QSize(40, 40))
        self.homeButton.setCheckable(True)
        self.homeButton.setChecked(True)
        self.homeButton.setAutoExclusive(True)
        self.homeButton.setObjectName("homeButton")
        self.calculatorButton = QtWidgets.QPushButton(parent=self.widget)
        self.calculatorButton.setGeometry(QtCore.QRect(10, 140, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calculatorButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/calculator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.calculatorButton.setIcon(icon1)
        self.calculatorButton.setIconSize(QtCore.QSize(40, 40))
        self.calculatorButton.setCheckable(True)
        self.calculatorButton.setAutoExclusive(True)
        self.calculatorButton.setObjectName("calculatorButton")
        self.designButton = QtWidgets.QPushButton(parent=self.widget)
        self.designButton.setGeometry(QtCore.QRect(10, 230, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.designButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/pencil.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.designButton.setIcon(icon2)
        self.designButton.setIconSize(QtCore.QSize(40, 40))
        self.designButton.setCheckable(True)
        self.designButton.setAutoExclusive(True)
        self.designButton.setObjectName("designButton")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 140, 451, 501))
        self.stackedWidget.setStyleSheet("QPushButton {\n"
"    background-color: rgb(119, 245, 207);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(88, 181, 152);\n"
"    border-radius:5px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_16 = QtWidgets.QLabel(parent=self.page)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 421, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_16.setFont(font)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.page)
        self.label_17.setGeometry(QtCore.QRect(20, 150, 381, 131))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("resources/stockImage2.jpg"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(parent=self.page)
        self.label_19.setGeometry(QtCore.QRect(20, 290, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(0, 112, 224)")
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(parent=self.page)
        self.label_18.setGeometry(QtCore.QRect(20, 330, 381, 141))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("resources/stockImage1.jpg"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_26 = QtWidgets.QLabel(parent=self.page)
        self.label_26.setGeometry(QtCore.QRect(20, 480, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(0, 112, 224)")
        self.label_26.setObjectName("label_26")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lineEditR0 = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditR0.setGeometry(QtCore.QRect(330, 80, 101, 21))
        self.lineEditR0.setObjectName("lineEditR0")
        self.lineEditKb = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditKb.setGeometry(QtCore.QRect(330, 40, 101, 21))
        self.lineEditKb.setObjectName("lineEditKb")
        self.lineEditG = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditG.setGeometry(QtCore.QRect(330, 120, 101, 21))
        self.lineEditG.setObjectName("lineEditG")
        self.pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(230, 280, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.label_12 = QtWidgets.QLabel(parent=self.page_2)
        self.label_12.setGeometry(QtCore.QRect(10, 300, 61, 16))
        self.label_12.setObjectName("label_12")
        self.lineEditCL = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditCL.setGeometry(QtCore.QRect(80, 300, 91, 21))
        self.lineEditCL.setObjectName("lineEditCL")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.page_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(160, 230, 271, 20))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(60)
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_10 = QtWidgets.QLabel(parent=self.page_2)
        self.label_10.setGeometry(QtCore.QRect(10, 190, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.page_2)
        self.label_11.setGeometry(QtCore.QRect(10, 230, 61, 16))
        self.label_11.setObjectName("label_11")
        self.lineEditMu = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditMu.setGeometry(QtCore.QRect(80, 40, 91, 21))
        self.lineEditMu.setObjectName("lineEditMu")
        self.lineEditTT = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditTT.setGeometry(QtCore.QRect(80, 230, 51, 21))
        self.lineEditTT.setObjectName("lineEditTT")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 340, 421, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(parent=self.page_2)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(parent=self.page_2)
        self.label_7.setGeometry(QtCore.QRect(270, 120, 51, 16))
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(parent=self.page_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditBD = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditBD.setGeometry(QtCore.QRect(330, 190, 101, 21))
        self.lineEditBD.setObjectName("lineEditBD")
        self.label_9 = QtWidgets.QLabel(parent=self.page_2)
        self.label_9.setGeometry(QtCore.QRect(240, 190, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(parent=self.page_2)
        self.label_13.setGeometry(QtCore.QRect(10, 270, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 31, 16))
        self.label_5.setObjectName("label_5")
        self.lineEditP = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditP.setGeometry(QtCore.QRect(80, 120, 91, 21))
        self.lineEditP.setObjectName("lineEditP")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(parent=self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 160, 191, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditTL = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditTL.setGeometry(QtCore.QRect(80, 190, 91, 21))
        self.lineEditTL.setObjectName("lineEditTL")
        self.label_6 = QtWidgets.QLabel(parent=self.page_2)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_6.setObjectName("label_6")
        self.lineEditQ = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEditQ.setGeometry(QtCore.QRect(80, 80, 91, 21))
        self.lineEditQ.setObjectName("lineEditQ")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.labelModel = QtWidgets.QLabel(parent=self.page_3)
        self.labelModel.setGeometry(QtCore.QRect(0, 200, 431, 301))
        self.labelModel.setText("")
        self.labelModel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.labelModel.setPixmap(QtGui.QPixmap("resources/Model2A.png"))
        self.labelModel.setScaledContents(True)
        self.labelModel.setObjectName("labelModel")
        self.T2Output = QtWidgets.QLabel(parent=self.page_3)
        self.T2Output.setGeometry(QtCore.QRect(290, 130, 31, 21))
        self.T2Output.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.T2Output.setText("")
        self.T2Output.setObjectName("T2Output")
        self.T1Output = QtWidgets.QLabel(parent=self.page_3)
        self.T1Output.setGeometry(QtCore.QRect(290, 80, 31, 21))
        self.T1Output.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.T1Output.setText("")
        self.T1Output.setObjectName("T1Output")
        self.label_14 = QtWidgets.QLabel(parent=self.page_3)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.chipSlot1 = QtWidgets.QRadioButton(parent=self.page_3)
        self.chipSlot1.setGeometry(QtCore.QRect(10, 80, 41, 20))
        self.chipSlot1.setCheckable(True)
        self.chipSlot1.setChecked(False)
        self.chipSlot1.setAutoExclusive(False)
        self.chipSlot1.setObjectName("chipSlot1")
        self.chipSlot2 = QtWidgets.QRadioButton(parent=self.page_3)
        self.chipSlot2.setGeometry(QtCore.QRect(10, 130, 41, 20))
        self.chipSlot2.setAutoExclusive(False)
        self.chipSlot2.setObjectName("chipSlot2")
        self.lineEditChip1 = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEditChip1.setGeometry(QtCore.QRect(60, 80, 91, 21))
        self.lineEditChip1.setObjectName("lineEditChip1")
        self.lineEditChip2 = QtWidgets.QLineEdit(parent=self.page_3)
        self.lineEditChip2.setGeometry(QtCore.QRect(60, 130, 91, 21))
        self.lineEditChip2.setObjectName("lineEditChip2")
        self.pushButtonDesign = QtWidgets.QPushButton(parent=self.page_3)
        self.pushButtonDesign.setGeometry(QtCore.QRect(340, 80, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonDesign.setFont(font)
        self.pushButtonDesign.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.pushButtonDesign.setObjectName("pushButtonDesign")
        self.label_20 = QtWidgets.QLabel(parent=self.page_3)
        self.label_20.setGeometry(QtCore.QRect(10, 50, 49, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.page_3)
        self.label_21.setGeometry(QtCore.QRect(70, 50, 71, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.page_3)
        self.label_22.setGeometry(QtCore.QRect(290, 50, 41, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.page_3)
        self.label_23.setGeometry(QtCore.QRect(260, 80, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.page_3)
        self.label_24.setGeometry(QtCore.QRect(260, 130, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.comboBoxChip1 = QtWidgets.QComboBox(parent=self.page_3)
        self.comboBoxChip1.setGeometry(QtCore.QRect(166, 80, 81, 22))
        self.comboBoxChip1.setObjectName("comboBoxChip1")
        self.comboBoxChip1.addItem("")
        self.comboBoxChip1.addItem("")
        self.comboBoxChip1.addItem("")
        self.comboBoxChip1.addItem("")
        self.comboBoxChip2 = QtWidgets.QComboBox(parent=self.page_3)
        self.comboBoxChip2.setGeometry(QtCore.QRect(166, 130, 81, 22))
        self.comboBoxChip2.setObjectName("comboBoxChip2")
        self.comboBoxChip2.addItem("")
        self.comboBoxChip2.addItem("")
        self.comboBoxChip2.addItem("")
        self.comboBoxChip2.addItem("")
        self.label_25 = QtWidgets.QLabel(parent=self.page_3)
        self.label_25.setGeometry(QtCore.QRect(190, 50, 41, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.stackedWidget.addWidget(self.page_3)
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(180, 30, 421, 101))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("resources/vivostream_logo.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application"))
        self.homeButton.setText(_translate("MainWindow", " Home"))
        self.calculatorButton.setText(_translate("MainWindow", " Calculator"))
        self.designButton.setText(_translate("MainWindow", " Design"))
        self.label_16.setText(_translate("MainWindow", "Our mission is to revolutionize microfluidics for organ-on-a-chip applications. We\'re dedicated to crafting accessible, adaptable perfusion systems that empower research and innovation. Our goal is to simplify complex experimentation, making scientific breakthroughs more achievable for all."))
        self.label_19.setText(_translate("MainWindow", "Learn more"))
        self.label_26.setText(_translate("MainWindow", "Learn more"))
        self.lineEditR0.setText(_translate("MainWindow", "1.0e-4"))
        self.lineEditKb.setText(_translate("MainWindow", "0.265"))
        self.lineEditG.setText(_translate("MainWindow", "9.81"))
        self.pushButton.setText(_translate("MainWindow", "RUN SCRIPT"))
        self.label_12.setText(_translate("MainWindow", "chip length"))
        self.lineEditCL.setText(_translate("MainWindow", "20e-2"))
        self.label_10.setText(_translate("MainWindow", "tube length"))
        self.label_11.setText(_translate("MainWindow", "tube turns"))
        self.lineEditMu.setText(_translate("MainWindow", "1.0016e-3"))
        self.lineEditTT.setText(_translate("MainWindow", "60"))
        self.label_4.setText(_translate("MainWindow", "r0 (m)"))
        self.label_7.setText(_translate("MainWindow", "g (m/s2)"))
        self.label.setText(_translate("MainWindow", "Fixed parameters for perfusion"))
        self.lineEditBD.setText(_translate("MainWindow", "25e-4"))
        self.label_9.setText(_translate("MainWindow", "bend diameter"))
        self.label_13.setText(_translate("MainWindow", "Fixed parameters for chip"))
        self.label_5.setText(_translate("MainWindow", "K_b"))
        self.lineEditP.setText(_translate("MainWindow", "1000"))
        self.label_2.setText(_translate("MainWindow", "mu (Pa.s)"))
        self.label_8.setText(_translate("MainWindow", "Tunable parameters for perfusion"))
        self.label_3.setText(_translate("MainWindow", "p (kg/m3)"))
        self.lineEditTL.setText(_translate("MainWindow", "50e-2"))
        self.label_6.setText(_translate("MainWindow", "Q (m3/s)"))
        self.lineEditQ.setText(_translate("MainWindow", "1.3888889e-12"))
        self.label_14.setText(_translate("MainWindow", "Perfusion design configuration"))
        self.chipSlot1.setText(_translate("MainWindow", "1"))
        self.chipSlot2.setText(_translate("MainWindow", "2"))
        self.lineEditChip1.setText(_translate("MainWindow", "2.8e-12"))
        self.lineEditChip2.setText(_translate("MainWindow", "1.4e-12"))
        self.pushButtonDesign.setText(_translate("MainWindow", "CALCULATE \n"
" DESIGN"))
        self.label_20.setText(_translate("MainWindow", "Chip"))
        self.label_21.setText(_translate("MainWindow", "Flow rate (Q)"))
        self.label_22.setText(_translate("MainWindow", "Coils"))
        self.label_23.setText(_translate("MainWindow", "→"))
        self.label_24.setText(_translate("MainWindow", "→"))
        self.comboBoxChip1.setItemText(0, _translate("MainWindow", "m^3/s"))
        self.comboBoxChip1.setItemText(1, _translate("MainWindow", "L/s"))
        self.comboBoxChip1.setItemText(2, _translate("MainWindow", "mL/s"))
        self.comboBoxChip1.setItemText(3, _translate("MainWindow", "uL/m"))
        self.comboBoxChip2.setItemText(0, _translate("MainWindow", "m^3/s"))
        self.comboBoxChip2.setItemText(1, _translate("MainWindow", "L/s"))
        self.comboBoxChip2.setItemText(2, _translate("MainWindow", "mL/s"))
        self.comboBoxChip2.setItemText(3, _translate("MainWindow", "uL/m"))
        self.label_25.setText(_translate("MainWindow", "Units"))
