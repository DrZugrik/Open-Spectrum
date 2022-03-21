from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import numpy

Form, Window = uic.loadUiType("gui.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
