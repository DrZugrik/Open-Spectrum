from PyQt5 import QtWidgets, uic
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.openSpec)

    def openSpec(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку")
        print(directory)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())