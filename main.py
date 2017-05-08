#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from gui import Ui_Widget
from PyQt5 import QtCore
from PyQt5 import QtGui


class Widgety(QWidget, Ui_Widget):
    """ Główna klasa aplikacji """

    def __init__(self, parent=None):
        super(Widgety, self).__init__(parent)



        self.setupUi(self)  # tworzenie interfejsu



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Widgety()
    okno.show()


    sys.exit(app.exec_())