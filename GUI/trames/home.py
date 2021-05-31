import os

from PySide2 import QtWidgets, QtGui, QtCore

from GUI.trames.definition_fonctions_d_utilite import DefinitionFonctionsDUtilite
from GUI.trames.saisie_joueurs_strategies import SaisieJoueursStrategies

i = 0


class Home(QtWidgets.QTabWidget):
    def __init__(self, appelant):
        super(Home, self).__init__()
        self.disposition = QtWidgets.QHBoxLayout()
        self.appelant = appelant

        ######TAB JOUEURS/STRATEGIES########
        self.trame1 = QtWidgets.QFrame()
        self.trame_jostr = SaisieJoueursStrategies(self)

        self.valider_jostr = QtWidgets.QPushButton("Valider")
        self.valider_jostr.setObjectName("valider")
        self.valider_jostr.setMaximumWidth(100)
        self.valider_jostr.setMinimumHeight(30)
        self.valider_jostr.clicked.connect(self.valider)

        hbox_trm_v = QtWidgets.QHBoxLayout()
        hbox_trm_v.addWidget(QtWidgets.QFrame())
        hbox_trm_v.addWidget(self.valider_jostr)
        self.trame_valide = QtWidgets.QFrame()
        self.trame_valide.setMaximumHeight(70)
        self.trame_valide.setLayout(hbox_trm_v)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.trame_jostr)
        vbox.addWidget(self.trame_valide)

        self.trame1.setLayout(vbox)

        self.addTab(self.trame1, "Definition des joueurs et des strategies")

    def valider(self):
        nb_joueurs = len(self.trame_jostr.frames) - 1

        nb_strategies_par_joueur = []

        for i in range(nb_joueurs):
            nb_strategies_par_joueur.append(self.trame_jostr.frames[i].j)

        self.definitionfonctionsdutilite = DefinitionFonctionsDUtilite(self, nb_strategies_par_joueur)

        self.addTab(self.definitionfonctionsdutilite, "Definition Fonctions D'Utilite")
