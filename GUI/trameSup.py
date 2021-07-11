import PySide2
from PySide2 import QtGui
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QFrame


class TrameSup(QFrame):
    def __init__(self, appelant):
        super(TrameSup, self).__init__()
        self.mainWindow = appelant

        hbox = QtWidgets.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        self.toggle_boutton = QtWidgets.QPushButton()
        self.toggle_boutton.setObjectName("toggle_but")
        self.toggle_boutton.clicked.connect(lambda: self.tog_fun(250))
        self.toggle_boutton.setMaximumHeight(70)
        self.toggle_boutton.setMaximumWidth(70)

        hbox.addWidget(self.toggle_boutton)
        f = QFrame()
        hbox.addWidget(f)

        self.setLayout(hbox)

        self.setMinimumSize(QtCore.QSize(0, 65))
        self.setMaximumSize(QtCore.QSize(1700, 65))

    def tog_fun(self, maxWidth):
        width = self.mainWindow.trameInf.barreLater_frame.width()
        maxExtend = maxWidth
        standard = 70

        # SET MAX WIDTH
        if width == 70:
            widthExtended = maxExtend
            self.mainWindow.trameInf.home_button.setText("Home")
            self.mainWindow.trameInf.affichage_principal.setText("Show")

        else:
            widthExtended = standard
            self.mainWindow.trameInf.home_button.setText("")
            self.mainWindow.trameInf.affichage_principal.setText("")

        self.animation = QtCore.QPropertyAnimation(self.mainWindow.trameInf.barreLater_frame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()