from PySide2 import QtWidgets
from PySide2.QtWidgets import QFrame, QTabWidget, QStackedWidget

from GUI.trames.home import Home
from GUI.trames.parametres import Parametres
from GUI.trames.traitements import Traitements


class TramePrincipale(QStackedWidget):
    def __init__(self, appelant):
        super(TramePrincipale, self).__init__()
        self.appelant = appelant

        # Home
        self.home = Home(self)
        self.home.setObjectName("home")

        # Affichage
        self.affichage = Traitements(self)

        # Parametres
        self.parametres_menu = Parametres(self)

        self.addWidget(self.home)
        self.addWidget(self.affichage)
        self.addWidget(self.parametres_menu)

        self.setFrameShape(QFrame.NoFrame)