from PyQt5 import QtWidgets
import pandas as pd
import sys

from pandas import DataFrame

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
        self._X = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonWeights.csv"))
        self._Y = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonTarget.csv"))
        # self.setStaticGraphData()
        self._graph1()
        self._graph2()
        self._graph3()

    # def setStaticGraphData(self):
    #     self.CRIME = []
    #     self.AGE = []
    #     self.IDK = []
    #     self.TARGET = []
    #     for l in x:
    #         self.AGE.append(l[6])
    #         self.CRIME.append(l[0])
    #         self.IDK.append(l[4])
    #     for l in y:
    #         self.TARGET.append((l[0])*10000)

    def _graph1(self):
        # set a new item to put int the widget
        x = range(0, 10)
        y = range(0, 20, 2)
        self._ui.widget.canvas.ax.plot(x, y)
        self._ui.widget.canvas.draw()


    def _graph2(self):
        # set a new item to put int the widget
        x = range(0, 10)
        y = range(0, 20, 2)
        self._ui.widget_2.canvas.ax.plot(x, y)
        self._ui.widget_2.canvas.draw()

    def _graph3(self):
        #     set a new item to put int the widget
        x = range(0, 10)
        y = range(0, 20, 2)
        self._ui.widget_3.canvas.ax.plot(x, y)
        self._ui.widget_3.canvas.draw()


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
