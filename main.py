from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import sys
import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.openSpec)

    def openSpec(self):
        v2=[]
        #fname = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл спектра")
        #path = fname[0]
        #print(path)
        path = 'TestPics/test1.jpg'
        pixmap = QPixmap(path)
        self.label.setPixmap(pixmap)

        im = Image.open(path)
        print(im.size)
        central_line = im.size[0] // 2
        print(central_line)
        im = im.crop((0, 60, im.size[1], 61))
        v = list(im.getdata())
        print(im.size)
        print(v)
        print(len(v))

        '''values = list(im.getdata())
        print(values)'''

        
        plt.title("Интенсивность излучения по линиям спектра") # заголовок
        plt.xlabel("Длина волны, нм") # ось абсцисс
        x = np.linspace(380, 780, len(v))

        plt.subplot(2, 1, 1)
        plt.ylabel("Интенсивность излучения RGB") # ось ординат
        plt.xlabel("Длина волны, нм") # ось абсцисс
        #x = np.linspace(0, 210, 50)
        plt.plot(x, v)
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.ylabel("Интенсивность излучения результирующая") # ось ординат
        plt.xlabel("Длина волны, нм") # ось абсцисс
        #x = np.linspace(0, 210, 50)
        plt.plot(x, v)
        plt.grid(True)
        plt.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()
    sys.exit(app.exec())
