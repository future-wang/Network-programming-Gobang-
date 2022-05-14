import sys# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt, QPoint
from Gobang import Ui_Form
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from board import Board
# from .threadServer import connectServer
from threadClient import connectClient



class LaBel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self, e):
        e.ignore()


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.black = QPixmap('Img/black.png')
        self.white = QPixmap('Img/white.png')
        self.pieces = [LaBel(self) for i in range(225)]
        self.initwidth = 325
        self.initheight = 35
        self.initstyp = 50
        self.board = Board()
        self.youturn = False
        self.steep = 0
        for piece in self.pieces:
            piece.setVisible(True)
            piece.setScaledContents(True)

        # button clicked event
        self.butConnect.clicked.connect(self.eventConnect)

    # def mouse
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == Qt.LeftButton:
            x, y = event.pos().x(), event.pos().y()
            if self.youturn == True and x > self.initwidth - 5 and y > self.initheight - 5:
                print(x, y)
                x_, y_, x, y = self.getPos(x, y)
                print(f'x_:{x_} y_:{y_}')

                if self.board.getstate(x, y):
                    print(self.steep)
                    self.board.draw(x, y, 1)
                    self.pieces[self.steep].setPixmap(self.selficon)
                    self.pieces[self.steep].setGeometry(x_, y_, 35, 35)
                    self.steep += 1

                    mes = f'{x} {y} {self.steep}'
                    self.thread.client.send(mes.encode("utf-8"))
                    self.youturn = False
                    self.plainTextEdit.appendPlainText(f'己方:({x + 1}, {y + 1})')
                    if self.board.isEnd(x, y, 1):
                        reply = QMessageBox.about(self, "消息框标题", "You Win!")
                    pass  # Is over?

    def getPos(self, x, y):
        locX = round((x - self.initwidth) / self.initstyp)
        locY = round((y - self.initheight) / self.initstyp)
        print(f'locX:{locX} locY:{locY}')
        return locX * self.initstyp + self.initwidth - 15, locY * self.initstyp + self.initheight - 15, locX, locY

    def eventConnect(self):
        print('Connect')
        IP = self.textIP.displayText()
        Port = self.textPort.displayText()
        self.thread = connectClient(IP=IP, Port=int(Port))
        self.thread.finishSignal.connect(self.drawAnother)
        self.thread.start()

    def drawAnother(self, rec):
        element = rec.split(' ')
        print(element)
        if len(element)<2 and element[0] == 'W':
            self.youturn = True
            self.selficon = self.black
            self.anothericon = self.white

            self.initstate = LaBel(self)
            self.initstate.setVisible(True)
            self.initstate.setScaledContents(True)
            self.initstate.setPixmap(self.selficon)
            self.initstate.setGeometry(70, 175, 35, 35)
        elif len(element)<2 and element[0] == 'B':
            self.youturn = False
            self.selficon = self.white
            self.anothericon = self.black

            self.initstate = LaBel(self)
            self.initstate.setVisible(True)
            self.initstate.setScaledContents(True)
            self.initstate.setPixmap(self.selficon)
            self.initstate.setGeometry(70, 175, 35, 35)
        if self.youturn == False and len(element) > 2:
            x = int(element[0])
            y = int(element[1])
            x_ = x * self.initstyp + self.initwidth - 15
            y_ = y * self.initstyp + self.initheight - 15
            # x_, y_ = int(element[0]) * self.initstyp + self.initwidth - 15, int(element[1]) * self.initstyp
            self.board.draw(x, y, 2)
            self.pieces[self.steep].setPixmap(self.anothericon)
            self.pieces[self.steep].setGeometry(x_, y_, 35, 35)
            self.steep += 1
            self.plainTextEdit.appendPlainText(f'对方:({x + 1}, {y + 1})')
            self.youturn = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # tmp = QWidget()
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
