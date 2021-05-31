import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout


class Traitements(QFrame):
    def __init__(self, appelant):
        super(Traitements, self).__init__()
        self.appelant = appelant

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

    def in2(self):
        self.tableau = self.appelant.home.definitionfonctionsdutilite.tableau
        frameTableau = QFrame()
        lo = QtWidgets.QHBoxLayout()
        lo.addWidget(self.tableau)
        frameTableau.setLayout(lo)

        frameInfos = QFrame()
        laout = QtWidgets.QVBoxLayout()
        # tableau pour les strategies dominantes pour chaque joueur

        self.layout.addWidget(frameTableau)
