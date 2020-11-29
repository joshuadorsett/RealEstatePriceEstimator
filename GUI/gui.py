from PyQt5 import QtWidgets
import pandas as pd
import sys

from pandas import DataFrame

from GUI.RealEstatePriceEstimator_ui import Ui_MainWindow

# use pyuic5 -o RealEstatePriceEstimator_ui.py RealEstatePriceEstimator.ui in the GUI folder every time you want to
# update ui design
# class for importing UI from QT Designer
from GUI.mplwidget import MplWidget
from oopModels.House import House


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # call inherited constructor
        super(Ui, self).__init__()
        # declare attributes for reference
        self._ui = None
        self._barChartMap = None
        self._houses = None
        self._houseAddress = None
        self._X = None
        self._Y = None
        # set up UI
        self._setUpUi()
        # Show the GUI
        self.show()

    def _setUpUi(self):
        self.setFixedSize(1640, 1040)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._actionHandling()
        self._csvToPandas()
        self._barChartMap = {"Min Price Sold": 50000.00, "Max Price Sold": 500000.00, "Mean Price Sold": 225328.06}
        self.comboBox1()
        self._setGraphs()

    # sets list of features into the combo box
    def comboBox1(self):
        features = ["Age of House", "Policing Rate", "Pupil-Teacher Ratio", "Property-Tax Rate", "Number of Rooms"]
        self._ui.selectFeature.addItems(features)

    # it first gathers all the saved houses in the database and puts them into a list
    # then set that list into the combo box
    def comboBox2(self):
        self._houses = []
        self._ui.savedHouses.addItems(self._houses)

    def _setGraphs(self):
        self._graph1()
        self._graph2()
        self._graph3()

    def _csvToPandas(self):
        self._X = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonWeights.csv"))
        self._Y = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonTarget.csv"))

    # plot canvas for embedded graph
    def _graph1(self):
        comboBoxText = self._ui.selectFeature.currentText()
        comboBoxIndex = self._ui.selectFeature.currentIndex()
        switcher = {0: 'CRIM', 1: 'AGE', 2: 'PTRATIO', 3: 'TAX', 4: 'RM'}
        self._ui.widget.canvas.ax.scatter(self._X[switcher[comboBoxIndex]], self._Y['0'] * 10000)
        self._ui.widget.canvas.ax.set(title=comboBoxText, xLabel=comboBoxText, yLabel="Price")
        self._ui.widget.canvas.draw()

    # plot canvas for embedded graph
    def _graph2(self):
        self._ui.widget_2.canvas.ax.bar(self._barChartMap.keys(), self._barChartMap.values())
        self._ui.widget_2.canvas.ax.set(title="Statistics", yLabel="Price")
        self._ui.widget_2.canvas.draw()

    # plot canvas for embedded graph
    def _graph3(self):
        self._ui.widget_3.canvas.ax.hist(self._Y['0'] * 10000, rwidth=0.6)
        self._ui.widget_3.canvas.ax.set(title="Prices Sold", xLabel="Prices Sold", yLabel="Volume")
        self._ui.widget_3.canvas.draw()

    def _actionHandling(self):
        # find and assign buttons
        self._ui.save.clicked.connect(self._saveMethod)
        self._ui.load.clicked.connect(self._loadMethod)
        self._ui.dele.clicked.connect(self._deleteMethod)
        self._ui.predict.clicked.connect(self._predictMethod)
        self._ui.selectFeatureButton.clicked.connect(self._selectFeatureMethod)

        # find and assign text fields
        self._houseAddress = self.findChild(QtWidgets.QLineEdit, "i0")

    def _saveMethod(self):
        print("save method")

    def _loadMethod(self):
        print(("load method"))

    def _deleteMethod(self):
        print("delete method")

    def _predictMethod(self):
        # create a new house object wit input text
        house = House(
            str(self._ui.i0_2.text()),
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
        self._ui.widget_2.canvas.ax.clear()
        self._barChartMap = {"Min Price Sold": 50000.00, "Max Price Sold": 500000.00, "Mean Price Sold": 225328.06,
                            "Predicted Price": float(predictionFloat)}
        self._ui.prediction.setText(str(predictionFloat))
        self._graph2()

    def _selectFeatureMethod(self):
        self._ui.widget.canvas.ax.clear()
        self._graph1()


# create app and window objects and then open GUI
app = QtWidgets.QApplication(sys.argv)  # Create an instance of app

window = Ui()  # create instance of Ui

app.exec()  # execute app
