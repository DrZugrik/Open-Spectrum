from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QPainter, QPen, QFont, QColor
from PyQt5.QtWidgets import QLabel, QSlider
import sys, os
import PIL
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import shutil
import threading


'''hsv_min = np.array((80, 0, 60), np.uint8)
hsv_max = np.array((255, 255, 255), np.uint8)'''





class mywindow(QtWidgets.QMainWindow):
    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.openSpec)
        self.pushButton_2.clicked.connect(self.drawSpec)
#        self.pushButton_3.clicked.connect(self.set_hsv)
        self.pushButton_2.setVisible(False)

        self.horizontalSlider.valueChanged[int].connect(self.hMin)
        self.horizontalSlider_2.valueChanged[int].connect(self.hMax)
        #self.horizontalSlider.valueChanged[int].connect(lambda value: self.label_2.setText(str(value)))
        #self.horizontalSlider_2.valueChanged[int].connect(lambda value: self.label_3.setText(str(value)))
        self.horizontalSlider_3.valueChanged[int].connect(self.sMin)
        self.horizontalSlider_4.valueChanged[int].connect(self.sMax)

        self.horizontalSlider_5.valueChanged[int].connect(self.vMin)
        self.horizontalSlider_6.valueChanged[int].connect(self.vMax)



        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setValue(1)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setValue(255)

        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setValue(1)
        self.horizontalSlider_4.setMaximum(255)
        self.horizontalSlider_4.setValue(255)

        self.horizontalSlider_5.setMaximum(255)
        self.horizontalSlider_5.setValue(1)
        self.horizontalSlider_6.setMaximum(255)
        self.horizontalSlider_6.setValue(255)

# ========================== Sliders ====================================++++++

    def hMin(self, value):
        global h_min
        value == 1
        self.label_2.setText(str(value))
        h_min = value

    def hMax(self, value):
        global h_max
        value == 255
        self.label_3.setText(str(value))
        h_max = value


    def sMin(self, value):
        global s_min
        value == 1
        self.label_10.setText(str(value))
        s_min = value

    def sMax(self, value):
        global s_max
        value == 255
        self.label_8.setText(str(value))
        s_max = value


    def vMin(self, value):
        global v_min
        value == 1
        self.label_11.setText(str(value))
        v_min = value

    def vMax(self, value):
        global v_max
        value == 255
        self.label_14.setText(str(value))
        v_max = value

# =============================================================================

    def openSpec(self):
        global v
        global im

        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл спектра")
        path = fname[0]
        #print(path)
        print('Open file spectrum')
        #print(f"hsv_max = {hsv_max}")


# ========================== Found contour ====================================

    # ============== Выводим фотку спектра с контуром =============================

        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(651, 431)
        self.label_4.setPixmap(pixmap)
        # print(f'pixmap = {type(pixmap)}')
        self.pushButton_2.setVisible(True)

        print('Draw pixmap without a contour')



        shutil.copyfile(path, 'temp_.jpg')
        img = cv.imread('temp_.jpg')
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV

        hsv_min_1 = np.array((h_min, s_min, v_min), np.uint8)
        hsv_max_1 = np.array((h_max, s_max, v_max), np.uint8)

        thresh = cv.inRange(hsv, hsv_min_1, hsv_max_1)  # применяем цветовой фильтр
        contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # ищем контуры
        '''print(type(hsv_min))
        print(type(hsv_max))'''

        '''print(f'hsv_min_1 = {hsv_min_1}')
        print(f'hsv_max_1 = {hsv_max_1}')'''


        # перебираем все найденные контуры в цикле
        for cnt in contours:
            rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат
            area = int(rect[1][0] * rect[1][1])  # вычисление площади
            if area > 500:
                cv.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник


        #cv.imshow('contours', img)  # вывод обработанного кадра в окно
        cv.imwrite('temp__.jpg', img)

        print('Try to found contour')


# ============== Выводим фотку спектра с контуром =============================

        pixmap = QPixmap('temp__.jpg')
        pixmap = pixmap.scaled(651, 431)
        self.label_4.setPixmap(pixmap)
        # print(f'pixmap = {type(pixmap)}')
        self.pushButton_2.setVisible(True)

        print('Draw pixmap with a contour')






# ============= Выбираем центральную линию контура ============================

        #self.lable.setPixmap(img)
        im = Image.open(path)
        #print(im.size)
        central_line = im.size[1] // 2
        #print(central_line)
        #print(f'Ширина = {im.size[0]}')
        #print(f'Высота = {im.size[1]}')

        im = im.crop((0, central_line, im.size[0], central_line+1))
        v = list(im.getdata())
        #print(im.size)
        #print(v)
        #print(len(v))
        im.close()

        print('Choose central line of spectr in counter')








# ============== Рисуем спектр из вектора =====================================

    def drawSpec(self):
        print('Draw spectrum')
        #print(f'spec = {v}')
        self.pushButton_2.setVisible(False)

        h = im.size[1]
        w = 651

        img = Image.new(mode="RGB", size=(len(v), h), color=0)
        #print(f'len(v) -- {len(v)}')
        for k in range(h):
            for p in range(len(v)):
                img.putpixel((p, k), v[p])




        qim = ImageQt(img)
        pix = QtGui.QPixmap.fromImage(qim)
        #print(f'img = {type(img)}')
        #print(f'qim = {type(qim)}')
        #print(f'pix = {type(pix)}')
        self.label.setPixmap(pix)

        print('Draw spectr from vector')


# =============== Собираем данные для отрисовки графиков ======================
        v2 = []
        for t in (v):
            t = (t[0] + t[1] + t[2]) // 3
            v2.append(t)
        # print(v2)

        plt.title("Интенсивность излучения по линиям спектра")  # заголовок
        plt.xlabel("Длина волны, нм")  # ось абсцисс
        x = np.linspace(380, 780, len(v))

        plt.subplot(2, 1, 1)
        plt.ylabel("Интенсивность излучения RGB")  # ось ординат
        plt.xlabel("Длина волны, нм")  # ось абсцисс
        # x = np.linspace(0, 210, 50)
        plt.plot(x, v)
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.ylabel("Интенсивность излучения результирующая")  # ось ординат
        plt.xlabel("Длина волны, нм")  # ось абсцисс
        # x = np.linspace(0, 210, 50)
        plt.plot(x, v2)
        plt.grid(True)
        #plt.show()

        print('Take data and draw charts')



# =============================================================================







if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.setFixedSize(964, 634)
    application.show()
    sys.exit(app.exec())
