# external modules
from PyQt5 import QtWidgets
import sys

# project modules
from FrontEnd.ui import Ui

if __name__ == "__main__":
    # create app and window objects and then open app
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Real Estate Price Estimator")
    app.exec()
