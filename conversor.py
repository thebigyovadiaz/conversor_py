#!/usr/bin/env python3
import sys

from PyQt4 import QtGui, uic

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("conversor.ui")[0]


class MiVentana(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.CtoF_Button.clicked.connect(self.ctof_button_click)
        self.FtoC_Button.clicked.connect(self.ftoc_button_click)

    # Evento del boton btn_CtoF
    def ctof_button_click(self):
        cel = float(self.CBox.text())
        fahr = cel * 9 / 5.0 + 32
        self.FBox.setValue(int(fahr + 0.5))

    # Evento del boton btn_FtoC
    def ftoc_button_click(self):
        fahr = self.FBox.value()
        cel = ((fahr - 32) * 5) / 9
        self.CBox.setText(str(cel))

app = QtGui.QApplication(sys.argv)
Ventana = MiVentana(None)
Ventana.show()
app.exec_()
