from PyQt5 import QtWidgets
from PyQt5.uic import pyuic
import sys


class Ui(QtWidgets.QMainWindow, pyuic):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        pyuic.loadUi('RealEstatePriceEstimator.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
