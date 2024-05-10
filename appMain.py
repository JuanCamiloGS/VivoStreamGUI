import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap

from appGUI import Ui_MainWindow
from appFunctions import *

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.resultPrinter)
        self.horizontalSlider.valueChanged.connect(self.numberUpdater)
        self.homeButton.clicked.connect(self.switchToHome)
        self.calculatorButton.clicked.connect(self.switchToCalculator)
        self.designButton.clicked.connect(self.switchToDesign)
        self.pushButtonDesign.clicked.connect(self.resultPrinterDesign)
        self.chipSlot1.clicked.connect(self.changeModelPixmap)
        self.chipSlot2.clicked.connect(self.changeModelPixmap)
        self.comboBoxGet.currentIndexChanged.connect(self.getIndexChanged)

    def numberUpdater(self):
        newVal = self.horizontalSlider.value()
        self.lineEditTT.setText(str(newVal))
    
    def getIndexChanged(self):
        index = self.comboBoxGet.currentIndex()
        if index == 0:
            self.lineEditH.setEnabled(False)
            self.comboBox9.setEnabled(False)
            self.lineEditTT.setEnabled(True)
            self.horizontalSlider.setEnabled(True)
        elif index == 1:
            self.lineEditTT.setEnabled(False)
            self.horizontalSlider.setEnabled(False)
            self.lineEditH.setEnabled(True)
            self.comboBox9.setEnabled(True)

    def resultPrinter(self):
        self.textBrowser.clear()

        index = self.comboBoxGet.currentIndex()

        Q = float(self.lineEditQ.text())
        r0 = float(self.lineEditR0.text())
        mu = float(self.lineEditMu.text())
        length = float(self.lineEditTL.text())
        p = float(self.lineEditP.text())
        k_b = float(self.lineEditKb.text())
        g = float(self.lineEditG.text())
        R_b = float(self.lineEditBD.text())
        n = float(self.lineEditTT.text())
        h = float(self.lineEditH.text())/100 #Due to default units being cm

        u = velocity(Q, r0)
        self.textBrowser.append('Velocity: ' + str(u) + ' m/s')

        res_length = resistance_length(mu, length, r0)
        self.textBrowser.append('Resistance for the length: ' + str(res_length) + ' Ohm')

        Rn = reynolds_number(p, u, r0, mu)
        self.textBrowser.append('Reynolds number: ' + str(Rn))

        Ff = friction_factor(Rn)
        self.textBrowser.append('Friction factor: ' + str(Ff))

        res_360 = resistance_360(Ff, p, Q, R_b, r0, k_b)
        self.textBrowser.append('Resistance for 360: ' + str(res_360) + ' Ohm')

        if index == 0:
            res_tot = resistance_perfusion(res_length, n, res_360)
            self.textBrowser.append('Total resistance of the system: ' + str(res_tot) + ' Ohm')

            dP = pressure_drop(res_tot, Q)
            self.textBrowser.append('The pressure drop: ' + str(dP) + ' Pa')

            h = reservoir_height(dP, p, u, g)
            self.textBrowser.append('The height of the reservoir: ' + str(h) + ' cm')
        elif index == 1:
            pressure = (h * p * g) - 0.5 * p * u ** 2
            self.textBrowser.append('The pressure of the system: ' + str(pressure) + ' Pa')

            new_n = (pressure/Q - res_length)/res_360
            self.textBrowser.append('The number of coils needed: ' + str(int(new_n)) + '')


    def changeModelPixmap(self):
        if self.chipSlot1.isChecked():
            if self.chipSlot2.isChecked():
                self.labelModel.setPixmap(QPixmap('resources/Model2D'))
            else:
                self.labelModel.setPixmap(QPixmap('resources/Model2B'))
        else:
            if self.chipSlot2.isChecked():
                self.labelModel.setPixmap(QPixmap('resources/Model2C'))
            else:
                self.labelModel.setPixmap(QPixmap('resources/Model2A'))


    def resultPrinterDesign(self):
        Q1 = float(self.lineEditChip1.text())
        p1 = float(self.lineEditMedium1.text())
        Q2 = float(self.lineEditChip2.text())
        p2 = float(self.lineEditMedium2.text())
        if self.chipSlot1.isChecked():
            self.T1Output.setText(str(coilsDesign(Q1, p1)))
        else:
            self.T1Output.setText("")

        if self.chipSlot2.isChecked():
            self.T2Output.setText(str(coilsDesign(Q2, p2)))
        else:
            self.T2Output.setText("")
    
    def switchToHome(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switchToCalculator(self):
        self.stackedWidget.setCurrentIndex(1)

    def switchToDesign(self):
        self.stackedWidget.setCurrentIndex(2)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())