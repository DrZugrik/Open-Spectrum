from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.openSpec)

    def openSpec(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл спектра")
        path = fname[0]
        #print(path)
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())
