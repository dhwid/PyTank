#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtGui
from PyQt5 import QtCore
from AI import *
from map import *


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        self.hexy =[]
        self.size = 100

        # Inicjalizacja mapy
        self.dimension = 7
        self.matrix = [[0 for w in range(self.dimension)] for h in range(self.dimension)]

        map = Map()
        map.fill_matrix(self.matrix)

        # kolor obramowania i wypełnienia w formacie RGB
        self.kolorO = QColor(0, 0, 0)
        self.kolorW = QColor(200, 30, 40)
        self.timer = QtCore.QBasicTimer()

        # Timer
        self.speed = 1000
        self.timer.start(self.speed, self)

        self.resize(1000, 1000)
        self.setWindowTitle('Widżety')


    def drawHex(self,i,j):

        self.x= (3**0.5 / 2)
        #self.size = 200
        odd_offset = 0

        if i%2:
            odd_offset = self.size/2 * self.x


        self.offsetx = self.size * j * self.x + odd_offset
        self.offsety = (self.size / 4 + self.size / 2)*i

        self.hexaPoints = [QtCore.QPoint(self.size / 2 * self.x + self.offsetx, 0 + self.offsety),
                           QtCore.QPoint(self.size * self.x + self.offsetx, self.size / 4 + self.offsety),
                           QtCore.QPoint(self.size * self.x + self.offsetx,
                                         self.size / 4 + self.size / 2 + self.offsety),
                           QtCore.QPoint(self.size / 2 * self.x + self.offsetx, self.size + self.offsety),
                           QtCore.QPoint(0 + self.offsetx, (self.size / 4 + self.size / 2) + self.offsety),
                           QtCore.QPoint(0 + self.offsetx, self.size / 4 + self.offsety)]

        return QtGui.QPolygon(self.hexaPoints)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.rysujFigury(e, qp)
        qp.end()

    def rysujFigury(self, e, qp):
        qp.setPen(self.kolorO)  # kolor obramowania
        qp.setBrush(self.kolorW)  # kolor wypełnienia
        qp.setRenderHint(QPainter.Antialiasing)  # wygładzanie kształtu

        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matrix[i][j] == 0:
                    self.hex = self.drawHex(i,j)
                    self.hexy.append(self.hex)

        self.size = self.hexy.__len__()

        for i in range(self.size):
            qp.drawPolygon(self.hexy[i])

        # for i in range(3):
        #     self.hex = self.drawHex(i)
        #     self.hexy.append(self.hex)
        #
        # self.size = self.hexy.__len__()
        # print(self.size)
        # self.a = self.size -2
        #
        # for i in range(self.a,self.size):
        #     qp.drawPolygon(self.hexy[i])


    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():
            print("repaint")
            #self.repaint()
        else:
            QtGui.QFrame.timerEvent(self, event)

class Ksztalty:
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    Rect, Ellipse, Polygon, Line = range(4)
