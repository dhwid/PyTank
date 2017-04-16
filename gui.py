#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtGui
from PyQt5 import QtCore
from AI import *
from map import *
from level_types import*
from tank import*


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        self.hexy =[]
        self.size = 50

        # Inicjalizacja mapy
        self.dimension = 20
        self.matrix = [[0 for w in range(self.dimension)] for h in range(self.dimension)]

        map = Map()
        map.fill_matrix(self.matrix)
        self.ai = AI()
        self.tank = Tank()

        # kolor obramowania i wypełnienia w formacie RGB
        self.kolorW = QColor(0,0,0)
        self.timer = QtCore.QBasicTimer()

        # Timer
        self.speed = 10
        self.timer.start(self.speed, self)

        self.resize(1000, 1000)
        self.setWindowTitle('Widżety')


    def drawHex(self,i,j):

        self.x= (3**0.5 / 2)
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
        self.kolorW = QColor(0, 0, 0)
        qp.setRenderHint(QPainter.Antialiasing)  # wygładzanie kształtu

        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matrix[i][j] == BlockType.EMPTY:
                    self.kolorW = QColor(0, 0, 0)
                elif self.matrix[i][j] == BlockType.BRICK:
                    self.kolorW =QColor(200, 30, 40)
                elif self.matrix[i][j] == BlockType.AGENT:
                    self.kolorW =QColor(200, 200, 40)
                elif self.matrix[i][j] == BlockType.OPPONENT:
                    self.kolorW =QColor(100, 200, 0)
                elif self.matrix[i][j] == BlockType.FAST:
                    self.kolorW = QColor(222, 213, 208)


                self.hexy.append(self.kolorW)
                self.hex = self.drawHex(i,j)
                self.hexy.append(self.hex)

        size = self.hexy.__len__()

        for i in range(0,size,2):
            qp.setBrush(self.hexy[i])
            i+=1
            qp.drawPolygon(self.hexy[i])
            qp.setRenderHint(QPainter.Antialiasing)

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():
            #self.ai.oponent(self.matrix,self.dimension)
            self.repaint()
        else:
            QtGui.QFrame.timerEvent(self, event)

    def keyPressEvent(self, e):
        key = e.key()
        self.tank.run(key,self.matrix,self.dimension)
        self.tank.shoot(key,self.matrix,self.dimension)
        print("wcisnalem")


class Ksztalty:
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    Rect, Ellipse, Polygon, Line = range(4)
