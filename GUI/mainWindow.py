import sys

import PySide2
from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from GUI.trameInf import TrameInf
from GUI.trameSup import TrameSup


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Application de certaines notions de la Theorie des Jeux")
        self.setWindowIcon(QtGui.QIcon("icons/Breezeicons.png"))

        self.trameSup = TrameSup(self)
        self.trameSup.setObjectName("frame_barresSup")
        self.trameInf = TrameInf()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.trameSup)
        self.vbox.addWidget(self.trameInf)
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)

        buff = QWidget()
        buff.setLayout(self.vbox)

        self.setCentralWidget(buff)

        # Initialisation de la fiche de style qss
        style = open("style_sheet.qss")
        StyleSheet = style.read()
        self.setStyleSheet(StyleSheet)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    available_geometry = app.desktop().availableGeometry(window)
    window.resize(available_geometry.width()*2/3, available_geometry.height()*2/3)

    window.show()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()