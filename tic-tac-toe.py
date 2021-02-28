#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5 import uic
import sys


class App(QWidget):
    
    def __init__(self):

        self.ui = uic.loadUi("untitled.ui")

        self.ui.show()

        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        self.list_btn = [self.ui.btn1, self.ui.btn2, self.ui.btn3,
                         self.ui.btn4, self.ui.btn5, self.ui.btn6,
                         self.ui.btn7, self.ui.btn8, self.ui.btn9]

        self.counter = 0

        self.ui.btn1.clicked.connect(lambda: self.game(0, 0, self.ui.btn1))
        self.ui.btn2.clicked.connect(lambda: self.game(0, 1, self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda: self.game(0, 2, self.ui.btn3))
        self.ui.btn4.clicked.connect(lambda: self.game(1, 0, self.ui.btn4))
        self.ui.btn5.clicked.connect(lambda: self.game(1, 1, self.ui.btn5))
        self.ui.btn6.clicked.connect(lambda: self.game(1, 2, self.ui.btn6))
        self.ui.btn7.clicked.connect(lambda: self.game(2, 0, self.ui.btn7))
        self.ui.btn8.clicked.connect(lambda: self.game(2, 1, self.ui.btn8))
        self.ui.btn9.clicked.connect(lambda: self.game(2, 2, self.ui.btn9))
        self.ui.btn_reset.clicked.connect(lambda: self.reset())
    
    def is_winner(self, player):
        winner = player*3 

        for cell in self.cells:
            if ''.join(cell) == winner:
                return True

        for cell in list(zip(*self.cells)):
            if ''.join(cell) == winner:
                return True

        if self.cells[0][0] + self.cells[1][1] + self.cells[2][2] == winner:
            return True

        if self.cells[0][2] + self.cells[1][1] + self.cells[2][0] == winner:
            return True

        return False
    
    def is_tie(self):
        for row in self.cells:
            if " " in row:
                return False
        return True
    
    def reset(self):
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for btn in self.list_btn:
            btn.setText(None)    
        self.counter = 0
    
    def game(self, row, column, btn):
        self.ui.label.clear()
        if self.cells[row][column] == " ":
            self.counter += 1
            if self.counter % 2 != 0:
                btn.setText("X")
                self.cells[row][column] = "X"
                if self.is_winner("X"):
                    self.ui.label.setText('X WON')
                    self.reset()
                elif self.is_tie():
                    self.ui.label.setText("Tie game!")
                    self.reset()
            else:
                btn.setText("O")
                self.cells[row][column] = "O"
                if self.is_winner("O"):
                    self.ui.label.setText('O WON')
                    self.reset()
                elif self.is_tie():
                    self.ui.label.setText("Tie game!")
                    self.reset()
        else:
            self.ui.label.setText("seat is taken")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
