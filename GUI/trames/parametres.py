from PySide2 import QtWidgets, QtCore

class Parametres(QtWidgets.QFrame):
    def __init__(self, appelant):
        super(Parametres, self).__init__()
        self.appelant = appelant

        layout = QtWidgets.QVBoxLayout()

        self.setLayout(layout)