import copy
import math
import os
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QTableWidgetItem
import global_modul

from strategie_dominante import *

class DefinitionFonctionsDUtilite(QtWidgets.QFrame):
    def __init__(self, appelant, t):
        super(DefinitionFonctionsDUtilite, self).__init__()
        self.disposition = QtWidgets.QHBoxLayout()
        self.appelant = appelant

        self.t = t
        global nb_strategies_pour_chaque_joeurs
        global_modul.nb_strategies_pour_chaque_joeurs = copy.deepcopy(t)

        self.tableau = QtWidgets.QTableWidget()

        self.row = 1
        for x in t:
            self.row = self.row * x

        self.tableau.setRowCount(self.row)
        self.tableau.setColumnCount(2 * len(t))

        labels = []
        for i in range(len(t)):
            labels.append("strategie de j"+str(i+1))
        for i in range(len(t)):
            labels.append("utilité pour j"+str(i+1))

        self.tableau.setHorizontalHeaderLabels(labels)

        r = self.row
        for i in range(len(t)):
            r = r / t[i]
            for j in range(self.row):
                newItem = QTableWidgetItem()
                newItem.setText("s" + str(i + 1) + ", " + str((math.floor((j)/r))%(t[i])+1))
                self.tableau.setItem(j, i, newItem)

        self.valider = QtWidgets.QPushButton("Valider")
        self.valider.setObjectName("valider")
        self.valider.setMaximumWidth(100)
        self.valider.setMinimumHeight(30)
        self.valider.clicked.connect(self.validation)

        hbox_trm_v = QtWidgets.QHBoxLayout()
        hbox_trm_v.addWidget(QtWidgets.QFrame())
        hbox_trm_v.addWidget(self.valider)
        self.trame_valide = QtWidgets.QFrame()
        self.trame_valide.setMaximumHeight(70)
        self.trame_valide.setLayout(hbox_trm_v)

        self.lo = QtWidgets.QVBoxLayout()
        self.lo.addWidget(self.tableau)
        self.lo.addWidget(self.trame_valide)

        self.setLayout(self.lo)

    def validation(self):
        table_utilites = {}
        for row in range(self.row):
            j = []
            for col in range(len(self.t)):
                j.append(int(self.tableau.item(row, col).text()[-1]))

            u = []
            for col in range(len(self.t), 2*len(self.t)):
                u.append(int(self.tableau.item(row, col).text()))

            table_utilites[tuple(j)] = tuple(u)

        global fonctions_dutilite
        global_modul.fonctions_dutilite = copy.deepcopy(table_utilites)

        self.appelant.appelant.appelant.aller_a_affichage_principal()

        self.appelant.appelant.appelant.frame_principale.affichage.in2()





