#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from AI import *
from map import *
from level_types import*
from tank import*
import numpy as np
from recording import*
from player_AI import *
import random


class Ui_Widget(object):
    """ Klasa definiująca GUI """

    def setupUi(self, Widget):

        self.hexy =[]
        self.size = 40
        self.key = 0
        self.agentHistory = []
        self.notReplay = True
        self.visitedX = []
        self.visitedY = []
        self.enableAI = False
        self.counter = 1

        #tworzenie xml
        self.history = History()


        # Inicjalizacja mapy
        self.dimension = 20
        self.matrix = [[0 for w in range(self.dimension)] for h in range(self.dimension)]
        self.changes = np.ones((self.dimension,self.dimension))

        # button = QPushButton('zapisz', self)
        # button.move(10,self.dimension*self.size*0.77 )
        # button.clicked.connect(self.saveToXML)
        #
        # button1 = QPushButton('powtorka', self)
        # button1.move(150,self.dimension*self.size*0.77 )
        # button1.clicked.connect(self.replay)

        button = QPushButton('AI', self)
        button.move(10,self.dimension*self.size*0.77 )
        button.clicked.connect(self.saveToXML)


        self.map = Map()
        self.map.fill_matrix(self.matrix)
        self.ai = AI()
        self.tank = Tank()

        # kolor obramowania i wypełnienia w formacie RGB
        self.kolorW = QColor(0,0,0)
        self.timer = QtCore.QBasicTimer()

        # Timer
        self.speed = 500
        self.timer.start(self.speed, self)


        width = self.dimension*self.size*0.9
        height = self.dimension*self.size*0.82
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
        self.rysujFigury(e, qp)
        qp.end()


    def rysujFigury(self, e, qp):
        self.kolorW = QColor(0, 0, 0)
        qp.setPen(QColor(0,0,0))
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

        self.drawGun(qp)

    def drawGun(self,qp):

        if ~Positions.AGENT_x%2:
            odd_offset = self.size/2 * self.x
        else: odd_offset = self.size * self.x

        self.offsetx = self.size * Positions.AGENT_y * self.x + odd_offset
        self.offsety = (self.size / 4 + self.size / 2)*Positions.AGENT_x

        x0 = self.offsetx
        y0 = self.size / 2 + self.offsety

        if Positions.AGENT_direction == Direction.RIGHT:
            x1 = x0 + self.size/2*self.x
            y1 = y0
        elif Positions.AGENT_direction == Direction.LEFT:
            x1 = x0 - self.size/2*self.x
            y1 = y0
        elif Positions.AGENT_direction == Direction.UP_RIGHT:
            x1 = x0 + self.size/4*self.x
            y1 = y0 - self.size/3
        elif Positions.AGENT_direction == Direction.UP_LEFT:
            x1 = x0 - self.size/4*self.x
            y1 = y0 - self.size/3
        elif Positions.AGENT_direction == Direction.DOWN_RIGHT:
            x1 = x0 + self.size/4*self.x
            y1 = y0 + self.size/3
        elif Positions.AGENT_direction == Direction.DOWN_LEFT:
            x1 = x0 - self.size/4*self.x
            y1 = y0 + self.size/3

        qp.drawLine(x0, y0, x1, y1)


    def timerEvent(self, event):

        if ((event.timerId() == self.timer.timerId()) and self.notReplay and not self.enableAI) :
            self.ai.oponent(self.matrix,self.dimension,self.changes,self.history)
            self.tank.run(self.key, self.matrix, self.dimension, self.changes, self.history)
            self.tank.shoot(self.key, self.matrix, self.dimension, self.changes)
            self.history.addAgent(str(self.key))
            self.key = 0
            self.repaint()
        elif(self.enableAI):
            if(self.counter ==10):
                self.visitedX.clear()
                self.visitedY.clear()
                self.search(Positions.AGENT_x, Positions.AGENT_y)
                self.counter=0

            self.key = random.randint(68,71)
            self.matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
            self.matrix[self.visitedX[self.counter]][self.visitedY[self.counter]] = BlockType.AGENT
            self.changes[Positions.AGENT_x][Positions.AGENT_y] = 1
            self.changes[self.visitedX[self.counter]][self.visitedY[self.counter]] = 1

            Positions.AGENT_x = self.visitedX[self.counter]
            Positions.AGENT_y = self.visitedY[self.counter]
            self.ai.oponent(self.matrix,self.dimension,self.changes,self.history)
            self.tank.shoot(self.key, self.matrix, self.dimension, self.changes)
            self.counter+=1
            if(self.counter>=self.visitedX.__len__()):
                self.enableAI = False
                self.visitedX.clear()
                self.visitedY.clear()
                self.counter = 0
            self.repaint()

        else:
            QtGui.QFrame.timerEvent(self, event)

    def keyPressEvent(self, e):
        self.key = e.key()
        #self.tank.run(key,self.matrix,self.dimension,self.changes,self.history)
        #self.tank.shoot(key,self.matrix,self.dimension,self.changes)
        self.repaint()


    def replayHandler(self):
        self.replay = True
        self.map.fill_matrix(self.matrix)
        self.changes = np.ones((self.dimension, self.dimension))
        self.history.parseXML(self.agentHistory)



    def saveToXML(self):
        self.counter = 0
        self.enableAI = not self.enableAI
        if(Positions.OPONENT_exist):
            self.search(Positions.AGENT_x, Positions.AGENT_y)
        if (self.visitedX.__len__()<2):
            self.enableAI = False
            self.visitedX.clear()
            self.visitedY.clear()

    def search(self,x,y):
        if self.matrix[x][y] == BlockType.OPPONENT:
            return True
        elif self.matrix[x][y] == BlockType.BRICK or self.matrix[x][y] == BlockType.FAST:
            return False
        elif self.matrix[x][y] == BlockType.VISTITED:
            return False

        self.matrix[x][y] = BlockType.VISTITED
        self.visitedX.append(x)
        self.visitedY.append(y)

        if ((x < self.dimension and self.search(x + 1, y))
            or (y > 0 and self.search(x, y - 1))
            or (x > 0 and self.search(x - 1, y))
            or (y < self.dimension and self.search(x+1,y))):
            return True

        return False

    def replay(self):
        self.replay = False
        self.matrix[Positions.AGENT_x][Positions.AGENT_y] = 0
        self.matrix[Positions.OPONENT_x][Positions.OPONENT_y] = 0
        Positions.AGENT_x = 0
        Positions.AGENT_y = 3
        Positions.OPONENT_x = 6
        Positions.OPONENT_y = 3
        Positions.OPONENT_exist = True
        self.map.fill_matrix(self.matrix)
        self.changes = np.ones((self.dimension, self.dimension))
        self.history.parseXML(self.agentHistory)
        for i in range(self.agentHistory.__len__()):
            print('Replay')
            key = int(self.agentHistory[i])
            self.ai.oponent(self.matrix, self.dimension, self.changes, self.history)
            self.tank.run(key, self.matrix, self.dimension, self.changes, self.history)
            self.tank.shoot(key, self.matrix, self.dimension, self.changes)
            self.repaint()
            time.sleep(0.5)
        self.notReplay = True

