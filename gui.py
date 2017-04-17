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
import numpy as np


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        self.hexy =[]
        self.size = 40

        # Inicjalizacja mapy
        self.dimension = 20
        self.matrix = [[0 for w in range(self.dimension)] for h in range(self.dimension)]
        self.changes = np.ones((self.dimension,self.dimension))

        map = Map()
        map.fill_matrix(self.matrix)
        self.ai = AI()
        self.tank = Tank()

        # kolor obramowania i wypełnienia w formacie RGB
        self.kolorW = QColor(0,0,0)
        self.timer = QtCore.QBasicTimer()

        # Timer
        self.speed = 1000
        self.timer.start(self.speed, self)

        width = self.dimension*self.size*0.9
        height = self.dimension*self.size*0.8
        self.resize(width,height)
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
        self.rysujFigury1(e, qp)
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

    def rysujFigury1(self, e, qp):
        self.kolorW = QColor(0, 0, 0)
        qp.setPen(QColor(0,200,0))
        qp.setRenderHint(QPainter.Antialiasing)  # wygładzanie kształtu

        for i in range(self.dimension):
            for j in range(self.dimension):
                if(self.changes[i][j]):
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

        self.changes = np.zeros((self.dimension, self.dimension))
        size = self.hexy.__len__()

        for i in range(0,size,2):
            qp.setBrush(self.hexy[i])
            i+=1
            qp.drawPolygon(self.hexy[i])
            qp.setRenderHint(QPainter.Antialiasing)

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():
            self.ai.oponent(self.matrix,self.dimension,self.changes)
            self.repaint()
        else:
            QtGui.QFrame.timerEvent(self, event)

    def keyPressEvent(self, e):
        key = e.key()
        self.tank.run(key,self.matrix,self.dimension,self.changes)
        self.tank.shoot(key,self.matrix,self.dimension,self.changes)
        self.repaint()



class Ksztalty:
    """ Klasa pomocnicza, symuluje typ wyliczeniowy """
    Rect, Ellipse, Polygon, Line = range(4)
