from PyQt5 import QtWidgets
import pandas as pd
import sys

from PyQt5.QtWidgets import QMessageBox

import DAO.dataBase
from pandas import DataFrame

from GUI.RealEstatePriceEstimator_ui import Ui_MainWindow

# use pyuic5 -o RealEstatePriceEstimator_ui.py RealEstatePriceEstimator.ui in the GUI folder every time you want to
# update ui design
# class for importing UI from QT Designer
from GUI.mplwidget import MplWidget
from oopModels.House import House


def _is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # call inherited constructor
        super(Ui, self).__init__()
        # declare attributes for reference
        self._ui = None
        self._barChartMap = None
        self._currentHouse = None
        self._houseAddress = None
        self._X = None
        self._Y = None
        self._userHouseSpecs = None
        # access database
        self.DB = DAO.dataBase.DB()
        # set up UI
        self._setUpUi()
        # Show the GUI
        self.show()

    def _setUpUi(self):
        self.setFixedSize(1650, 1040)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._actionHandling()
        self._csvToPandas()
        self._barChartMap = {"Min Price Sold": 50000.00, "Max Price Sold": 500000.00, "Mean Price Sold": 225328.06}
        self.selectFeatureCB()
        self.savedHousesCB()
        self._setGraphs()

    # sets list of features into the combo box
    def selectFeatureCB(self):
        self._ui.selectFeature.clear()
        features = ["Age of House", "Policing Rate", "Pupil-Teacher Ratio", "Property-Tax Rate", "Number of Rooms"]
        self._ui.selectFeature.addItems(features)

    # it first gathers all the saved houses in the database and puts them into a list
    # then set that list into the combo box
    def savedHousesCB(self):
        self._ui.savedHouses.clear()
        sel = self.DB.selectAll()
        self.addressList = []
        for s in sel:
            self.addressList.append(s[1])
        self._ui.savedHouses.addItems(self.addressList)


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
    def _graph3(self):
        self._ui.widget_3.canvas.ax.set_facecolor((.84, .84, .84, 1))
        comboBoxText = self._ui.selectFeature.currentText()
        comboBoxIndex = self._ui.selectFeature.currentIndex()
        switcher = {0: 'CRIM', 1: 'AGE', 2: 'PTRATIO', 3: 'TAX', 4: 'RM'}
        self._ui.widget_3.canvas.ax.scatter(self._X[switcher[comboBoxIndex]], self._Y['0'] * 10000, color='black')
        if self._userHouseSpecs is not None:
            self._ui.widget_3.canvas.ax.scatter(self._userHouseSpecs[comboBoxIndex], self._userHouseSpecs[5], color='red', s=120, marker='o')
        self._ui.widget_3.canvas.ax.set(title=comboBoxText, xLabel=comboBoxText)
        self._ui.widget_3.canvas.draw()

    # plot canvas for embedded graph
    def _graph2(self):
        self._ui.widget_2.canvas.ax.set_facecolor((.84, .84, .84, 1))
        self._ui.widget_2.canvas.ax.bar(self._barChartMap.keys(), self._barChartMap.values(), color='blue')
        self._ui.widget_2.canvas.ax.set(title="Statistics")
        self._ui.widget_2.canvas.draw()

    # plot canvas for embedded graph
    def _graph1(self):
        self._ui.widget.canvas.ax.set_facecolor((.84, .84, .84, 1))
        self._ui.widget.canvas.ax.hist(self._Y['0'] * 10000, rwidth=0.6, color='green')
        self._ui.widget.canvas.ax.set(title="Prices Sold", xLabel="Prices Sold", yLabel="Volume")
        self._ui.widget.canvas.draw()

    def _actionHandling(self):
        # find and assign buttons
        self._ui.predict.clicked.connect(self._predictMethod)
        self._ui.selectFeatureButton.clicked.connect(self._selectFeatureMethod)
        # self._ui.save.clicked.connect(self._saveMethod)
        self._ui.load.clicked.connect(self._loadMethod)
        self._ui.dele.clicked.connect(self._deleteMethod)
        # find and assign text fields
        self._houseAddress = self.findChild(QtWidgets.QLineEdit, "i0")

    def messageBoxForInputs(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid Inputs.")
        msg.setText("Please input numbers in all fields.")
        msg.setStyleSheet("background-color: 'white';")
        msg.exec()

    def _predictMethod(self):
        if (self._ui.i0_2.text()) == '':
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i1.text()) == '') and (_is_float(self._ui.i1.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i2.text()) == '') and (_is_float(self._ui.i2.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i3.text()) == '') and (_is_float(self._ui.i3.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i4.text()) == '') and (_is_float(self._ui.i4.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i5.text()) == '') and (_is_float(self._ui.i5.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i6.text()) == '') and (_is_float(self._ui.i6.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i7.text()) == '') and (_is_float(self._ui.i7.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i8.text()) == '') and (_is_float(self._ui.i8.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i9.text()) == '') and (_is_float(self._ui.i9.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i10.text()) == '') and (_is_float(self._ui.i10.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i11.text()) == '') and (_is_float(self._ui.i11.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i12.text()) == '') and (_is_float(self._ui.i12.text()))):
            self.messageBoxForInputs()
            return
        if not (not ((self._ui.i13.text()) == '') and (_is_float(self._ui.i13.text()))):
            self.messageBoxForInputs()
            return
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
        self.DB.insert(house)
        self.savedHousesCB()
        self._ui.widget_2.canvas.ax.clear()
        self._ui.widget_3.canvas.ax.clear()
        self._barChartMap = {"Min Price Sold": 50000.00, "Max Price Sold": 500000.00, "Mean Price Sold": 225328.06,
                            "Predicted Price": float(predictionFloat)}
        self._ui.prediction.setText(str(predictionFloat))
        self._graph2()
        self._userHouseSpecs = [
            house.houseSpecs[0][0],
            house.houseSpecs[0][6],
            house.houseSpecs[0][10],
            house.houseSpecs[0][9],
            house.houseSpecs[0][5],
            float(predictionFloat)
            ]
        self._graph3()



    def _selectFeatureMethod(self):
        self._ui.widget_3.canvas.ax.clear()
        self._graph3()

    def _loadMethod(self):
        selAddress = self._ui.savedHouses.currentText()
        if selAddress is not '':
            house = self.DB.select(selAddress)
            print(house)
            self._ui.i0_2.setText(str(house[1]))
            self._ui.i1.setText(str(house[2]))
            self._ui.i2.setText(str(house[3]))
            self._ui.i3.setText(str(house[4]))
            self._ui.i4.setText(str(house[5]))
            self._ui.i5.setText(str(house[6]))
            self._ui.i6.setText(str(house[7]))
            self._ui.i7.setText(str(house[8]))
            self._ui.i8.setText(str(house[9]))
            self._ui.i9.setText(str(house[10]))
            self._ui.i10.setText(str(house[11]))
            self._ui.i11.setText(str(house[12]))
            self._ui.i12.setText(str(house[13]))
            self._ui.i13.setText(str(house[14]))
            self._predictMethod()
            self._selectFeatureMethod()
        else:
            pass

    def _deleteMethod(self):
        selAddress = self._ui.savedHouses.currentText()
        self.DB.delete(selAddress)
        self.savedHousesCB()

# create app and window objects and then open GUI
app = QtWidgets.QApplication(sys.argv)  # Create an instance of app

window = Ui()  # create instance of Ui

window.setWindowTitle("Real Estate Price Estimator")

app.exec()  # execute app


