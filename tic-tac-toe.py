#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import sys


class App(QWidget):
    def __init__(self):
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi("untitled.ui")
        self.ui.show()

    def set(self):
        self.ui.btn1.clicked.connect(lambda: self.display("button 1 pressed"))
        self.ui.btn2.clicked.connect(lambda: self.display("button 2 pressed"))
        self.ui.btn3.clicked.connect(lambda: self.display("button 3 pressed"))
        self.ui.btn4.clicked.connect(lambda: self.display("button 4 pressed"))
        self.ui.btn5.clicked.connect(lambda: self.display("button 5 pressed"))
        self.ui.btn6.clicked.connect(lambda: self.display("button 6 pressed"))
        self.ui.btn7.clicked.connect(lambda: self.display("button 7 pressed"))
        self.ui.btn8.clicked.connect(lambda: self.display("button 8 pressed"))
        self.ui.btn9.clicked.connect(lambda: self.display("button 9 pressed"))
        self.ui.btn_reset.clicked.connect(lambda: self.display("button reset"))

    def display(self, win):
        self.ui.label.setText(str(win))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()