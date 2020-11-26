from PyQt5 import QtWidgets
import pandas as pd
import sys

from GUI.RealEstatePriceEstimator_ui import Ui_MainWindow

# use pyuic5 -o RealEstatePriceEstimator_ui.py RealEstatePriceEstimator.ui in the GUI folder every time you want to
# update ui design
# class for importing UI from QT Designer
from oopModels.House import House


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # call inherited constructor
        self._setUpUi()
        self.show()  # Show the GUI

    def _setUpUi(self):
        self.setFixedSize(1540, 1020)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._actionHandling()
        self.x = [6,5,3,6,4]
        self.y = [9,3,5,2,6]
        self._dfX = pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonWeights.csv")
        self._dfY = pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonTarget.csv")
        self._graph1()
        self._graph2()
        self._graph3()

    def _graph1(self):
        dfX = pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonWeights.csv")
        dfY = pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonTarget.csv")
        self._ui.widget.plot(self.x, self.y)

    def _graph2(self):
        self._ui.widget_2.plot(self.x, self.y)

    def _graph3(self):
        self._ui.widget_3.plot(self.x, self.y)


    def _actionHandling(self):
        # find and assign buttons
        self._ui.save.clicked.connect(self._saveMethod)
        self._ui.load.clicked.connect(self._loadMethod)
        self._ui.dele.clicked.connect(self._deleteMethod)
        self._ui.predict.clicked.connect(self._predictMethod)

        # find and assign text fields
        self.houseAddress = self.findChild(QtWidgets.QLineEdit, "i0")

    def _saveMethod(self):
        print("save method")

    def _loadMethod(self):
        print(("load method"))

    def _deleteMethod(self):
        print("delete method")

    def _predictMethod(self):
        # create a new house object wit input text
        house = House(
                      float(self._ui.i1.text()),
                      float(self._ui.i2.text()),
                      float(self._ui.i3.text()),
                      float(self._ui.i4.text()),
                      float(self._ui.i5.text()),
                      float(self._ui.i6.text()),
                      float(self._ui.i7.text()),
                      float(self._ui.i8.text()),
                      float(self._ui.i9.text()),
                      float(self._ui.i10.text()),
                      float(self._ui.i11.text()),
                      float(self._ui.i12.text()),
                      float(self._ui.i13.text())
                      )

        # call ML method in House object and then set the prediction into the GUI
        predictionFloat64 = house.getLinearPrediction()
        predictionFloat = "{:.2f}".format(predictionFloat64)
        self._ui.prediction.setText(str(predictionFloat))


# create app and window objects and then open GUI
app = QtWidgets.QApplication(sys.argv)  # Create an instance of app

window = Ui()  # create instance of Ui

app.exec()  # execute app
