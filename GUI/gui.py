from PyQt5 import QtWidgets
from PyQt5 import uic
import sys


# class for importing UI from QT Designer
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # call inherited constructor
        uic.loadUi('RealEstatePriceEstimator.ui', self)  # Load .ui
        self.show()  # Show the GUI


# create app and window objects and then open GUI
app = QtWidgets.QApplication(sys.argv)  # Create an instance of app
window = Ui()  # create instance of Ui
app.exec()  # execute app
