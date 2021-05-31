import copy
import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout, QTableWidgetItem, QTableWidget
import global_modul

from strategie_dominante import strategie_dominante


class Traitements(QFrame):
    def __init__(self, appelant):
        super(Traitements, self).__init__()
        self.appelant = appelant

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    def in2(self):
        global nb_strategies_pour_chaque_joeurs
        global fonctions_dutilite

        print("donnees du jeu : ")
        print(global_modul.nb_strategies_pour_chaque_joeurs)
        print(global_modul.fonctions_dutilite)

        self.tableau = QTableWidget()
        self.tableau.setRowCount(self.appelant.home.definitionfonctionsdutilite.tableau.rowCount())
        self.tableau.setColumnCount(self.appelant.home.definitionfonctionsdutilite.tableau.columnCount())

        for i in range(self.appelant.home.definitionfonctionsdutilite.tableau.columnCount()):
            for j in range(self.appelant.home.definitionfonctionsdutilite.tableau.rowCount()):
                newItem = QTableWidgetItem()
                newItem.setText(self.appelant.home.definitionfonctionsdutilite.tableau.item(j, i).text())
                self.tableau.setItem(j, i, newItem)

        frameTableau = QFrame()
        lo = QtWidgets.QVBoxLayout()
        lo.addWidget(QLabel("Donnees du jeu"))
        lo.addWidget(self.tableau)
        frameTableau.setLayout(lo)

        frameInfos = QFrame()
        laout = QtWidgets.QVBoxLayout()
        # tableau pour les strategies dominantes pour chaque joueur
        self.strategies_dom = QTableWidget()
        self.strategies_dom.setRowCount(len(global_modul.nb_strategies_pour_chaque_joeurs))
        self.strategies_dom.setColumnCount(2)

        for i in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
            newItem = QTableWidgetItem()
            newItem.setText("J"+str(i+1))
            self.strategies_dom.setItem(i, 0, newItem)

            newItem = QTableWidgetItem()

            sd = strategie_dominante(i+1, global_modul.nb_strategies_pour_chaque_joeurs[i], global_modul.fonctions_dutilite)
            print("joueur " + str(i+1) + "strategie dominante : " + str(sd))

            newItem.setText("s" + str(i+1) + ", " + str(sd))
            self.strategies_dom.setItem(i, 1, newItem)

        laout.addWidget(QLabel("strategies dominantes :"))
        laout.addWidget(self.strategies_dom)
        frameInfos.setLayout(laout)

        self.layout.addWidget(frameTableau)
        self.layout.addWidget(frameInfos)

