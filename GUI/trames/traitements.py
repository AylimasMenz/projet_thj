import copy
import sys
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QTextBrowser, QFrame, QLabel, QVBoxLayout, QTableWidgetItem, QTableWidget
import global_modul
from eeisd import eeisd
from equilibre_de_nash import determinationDesEquilibresDeNash
from niveau_de_securite import niveauDeSecuriteStrategie, niveauDeSecuriteJoueur
from pareto_dominance import n_est_pas_pareto_domine_par, determinationDesOptimumsDePareto

from strategie_dominante import strategie_dominante
from global_modul import nb_strategies_pour_chaque_joeurs, fonctions_dutilite


class Traitements(QFrame):
    def __init__(self, appelant):
        super(Traitements, self).__init__()
        self.appelant = appelant

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

    def in2(self):
        global nb_strategies_pour_chaque_joeurs
        global fonctions_dutilite

        print("Donnees du jeu : ")
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

        # FRAME TABLEAU
        frameTableau = QFrame()
        lo = QtWidgets.QVBoxLayout()
        lo.addWidget(QLabel("Donnees du jeu"))
        lo.addWidget(self.tableau)
        frameTableau.setLayout(lo)

        # FRAME STRATEGIES DOMINANTES
        frameStrategiesDominantes = QFrame()
        laout = QtWidgets.QVBoxLayout()

        laout.addWidget(QLabel("Equilibre en Strategies Dominantes :"))

        for i in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
            sd = strategie_dominante(i+1, global_modul.nb_strategies_pour_chaque_joeurs[i], global_modul.fonctions_dutilite)
            laout.addWidget(QLabel("Joueur"+str(i+1) + " : " + str(sd)))
            print("joueur " + str(i+1) + "strategie dominante : " + str(sd))


        frameStrategiesDominantes.setLayout(laout)

        # FRAME EQUILIBRES DE NASH
        equilibresDeNash = determinationDesEquilibresDeNash()

        print("equilibres de Nash : ", equilibresDeNash)
        frameEquiNash = QFrame()
        loEN = QtWidgets.QVBoxLayout()
        loEN.addWidget(QLabel("Equilibres de Nash"))
        for en in equilibresDeNash:
            loEN.addWidget(QLabel(str(en)))

        frameEquiNash.setLayout(loEN)

        # PARETO DOMINANCE
        optimumsDePareto = determinationDesOptimumsDePareto()
        print("optimums De Pareto : ", optimumsDePareto)

        framePareto = QFrame()
        loPareto = QtWidgets.QVBoxLayout()
        loPareto.addWidget(QLabel("Optimums De Pareto"))
        for op in optimumsDePareto:
            loPareto.addWidget(QLabel(str(op)))

        framePareto.setLayout(loPareto)

        # NIVEAU DE SECURITÉ
        frameNiveauSecu = QFrame()
        loNiveauSecu = QVBoxLayout()

        for joueur in range(len(global_modul.nb_strategies_pour_chaque_joeurs)):
            loNiveauSecu.addWidget(QLabel("niveau de securite du joueur " + str(joueur+1) + " : " + str(niveauDeSecuriteJoueur(joueur))))
            for strategie in range(global_modul.nb_strategies_pour_chaque_joeurs[joueur]):
                loNiveauSecu.addWidget(QLabel("niveau de securite de la strategie s" + str(joueur+1) + ", " + str(strategie+1) + " : " + str(niveauDeSecuriteStrategie(joueur, strategie+1))))

        frameNiveauSecu.setLayout(loNiveauSecu)

        # EEISD
        print(global_modul.nb_strategies_pour_chaque_joeurs)
        print(global_modul.fonctions_dutilite)
        eeisdv = eeisd()
        print("EEISD : ", eeisdv)

        frameEEISD = QFrame()
        loEEISD = QtWidgets.QVBoxLayout()
        loEEISD.addWidget(QLabel("Equilibre Iteratif en Strategies Dominantes"))
        loEEISD.addWidget(QLabel(str(eeisdv)))

        frameEEISD.setLayout(loEEISD)

        # REUNION DES FRAMES
        self.layout.addWidget(frameTableau)
        self.layout.addWidget(frameStrategiesDominantes)
        self.layout.addWidget(frameEEISD)
        self.layout.addWidget(frameEquiNash)
        self.layout.addWidget(framePareto)
        self.layout.addWidget(frameNiveauSecu)


