import os

from PySide2 import QtWidgets, QtGui, QtCore

i = 0


class SaisieJoueursStrategies(QtWidgets.QFrame):
    def __init__(self, appelant):
        super(SaisieJoueursStrategies, self).__init__()
        self.disposition = QtWidgets.QHBoxLayout()
        self.appelant = appelant

        self.frame_ajout = FramePlus(self)

        self.frames = []
        self.frames.append(FrameJoueur(self))
        self.frames.append(FrameJoueur(self))
        self.frames.append(self.frame_ajout)

        self.ponereLayout()

    def ponereLayout(self):
        for frame in self.frames:
            self.disposition.addWidget(frame)

        self.fc = QtWidgets.QFrame()
        self.disposition.addWidget(self.fc)

        self.setLayout(self.disposition)


class FrameJoueur(QtWidgets.QFrame):
    def __init__(self, appelant):
        super(FrameJoueur, self).__init__()

        self.vbox = QtWidgets.QVBoxLayout()

        global i
        i = i + 1

        self.strategies = []
        self.j = 0

        self.ji = QtWidgets.QLabel("Joueur " + str(i))
        self.ji.setAlignment(QtCore.Qt.AlignCenter)

        self.plus_button = QtWidgets.QPushButton()
        self.plus_button.setObjectName("plus")
        self.plus_button.clicked.connect(self.plus)

        self.ji.setMaximumHeight(40)
        self.plus_button.setMaximumHeight(40)

        self.fc = QtWidgets.QFrame()

        self.vbox.addWidget(self.ji)
        self.vbox.addWidget(self.plus_button)
        self.vbox.addWidget(self.fc)

        self.setLayout(self.vbox)
        self.setMaximumWidth(150)

        self.plus()


    def plus(self):
        self.vbox.removeWidget(self.plus_button)
        self.vbox.removeWidget(self.fc)

        self.j = self.j + 1
        strateg = QtWidgets.QLabel("Strategie " + str(self.j))
        strateg.setAlignment(QtCore.Qt.AlignCenter)
        strateg.setMaximumHeight(40)

        self.strategies.append(strateg)

        self.vbox.addWidget(self.strategies[-1])
        self.vbox.addWidget(self.plus_button)
        self.vbox.addWidget(self.fc)



class FramePlus(QtWidgets.QFrame):
    def __init__(self, appelant):
        super(FramePlus, self).__init__()
        self.appelant = appelant

        vbox = QtWidgets.QVBoxLayout()

        plus = QtWidgets.QPushButton()
        plus.setObjectName("plus")
        plus.setMaximumHeight(40)
        plus.clicked.connect(self.plus)

        fc = QtWidgets.QFrame()

        vbox.addWidget(plus)
        vbox.addWidget(fc)

        self.setLayout(vbox)
        self.setMaximumWidth(150)

    def plus(self):
        self.appelant.frames.insert(-1, FrameJoueur(self.appelant))
        self.appelant.disposition.removeWidget(self.appelant.frames[-1])
        self.appelant.disposition.removeWidget(self.appelant.fc)

        self.appelant.disposition.addWidget(self.appelant.frames[-2])
        self.appelant.disposition.addWidget(self.appelant.frames[-1])
        self.appelant.disposition.addWidget(self.appelant.fc)
