import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

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

    def numberUpdater(self):
        newVal = self.horizontalSlider.value()
        self.lineEditTT.setText(str(newVal))

    def resultPrinter(self):
        self.textBrowser.clear()

        Q = float(self.lineEditQ.text())
        r0 = float(self.lineEditR0.text())
        mu = float(self.lineEditMu.text())
        length = float(self.lineEditTL.text())
        p = float(self.lineEditP.text())
        k_b = float(self.lineEditKb.text())
        g = float(self.lineEditG.text())
        R_b = float(self.lineEditBD.text())
        n = float(self.lineEditTT.text())
        length_chip = float(self.lineEditCL.text())

        u = velocity(Q, r0)
        self.textBrowser.append('Velocity: ' + str(u) + 'm/s')

        res_length = resistance_length(mu, length, r0)
        self.textBrowser.append('Resistance for the length: ' + str(res_length) + ' Ohm')

        Rn = reynolds_number(p, u, r0, mu)
        self.textBrowser.append('Reynolds number: ' + str(Rn))

        Ff = friction_factor(Rn)
        self.textBrowser.append('Friction factor: ' + str(Ff))

        res_180 = resistance_180(Ff, p, Q, R_b, r0, k_b)
        self.textBrowser.append('Resistance for 180: ' + str(res_180) + ' Ohm')

        res_90 = resistance_90(Ff, p, Q, R_b, r0, k_b)
        self.textBrowser.append('Resistance for 180: ' + str(res_90) + ' Ohm')

        res_perfusion = resistance_perfusion(res_length, n, res_180, res_90)
        self.textBrowser.append('Total resistance perfusion system: ' + str(res_perfusion) + ' Ohm')

        res_chip = resistance_chip(mu, length_chip, r0)
        self.textBrowser.append('Resistance of chip to waste: ' + str(res_chip) + ' Ohm')

        res_tot = total_resistance(res_perfusion, res_chip)
        self.textBrowser.append('Total resistance of the system: ' + str(res_tot) + ' Ohm')

        dP = pressure_drop(res_tot, Q)
        self.textBrowser.append('The pressure drop: ' + str(dP) + ' Pa')

        h = reservoir_height(dP, p, u, g)
        self.textBrowser.append('The height of the reservoir: ' + str(h) + ' cm')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())