# external modules
from PyQt5 import QtWidgets
import pandas as pd
import sys

# project modules
import BackEnd.database
# use pyuic5 -o RealEstatePriceEstimator_ui.py RealEstatePriceEstimator.ui
# in the FrontEnd folder to convert Ui to python file
from FrontEnd.RealEstatePriceEstimator_ui import Ui_MainWindow
from BackEnd.house import House
from FrontEnd.inputValidation import inputNotValid, messageBoxForIDInput


# class for importing UI from QT Designer
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # call inherited constructor
        super(Ui, self).__init__()
        # access database
        self.DB = BackEnd.database.DB()
        # set up UI
        self._setUpUi()
        # Show the FrontEnd
        self.show()

    # secondary constructor for setting up the Ui
    def _setUpUi(self):
        self._userHouseSpecs = None
        self.setFixedSize(1570, 1030)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._actionHandling()
        self._csvToPandas()
        self._barChartMap = {"Min Price Sold": 50000.00, "Max Price Sold": 500000.00, "Mean Price Sold": 225328.06}
        self.selectFeatureComboBox()
        self.savedHousesComboBox()
        self._setGraphs()

    # sets list of features into the combo box
    def selectFeatureComboBox(self):
        self._ui.selectFeature.clear()
        features = ["Age of House", "Policing Rate", "Pupil-Teacher Ratio", "Property-Tax Rate", "Number of Rooms"]
        self._ui.selectFeature.addItems(features)

    # gathers all the saved houses in the database and puts them into a list
    # then sets list into the combo box
    def savedHousesComboBox(self):
        self._ui.savedHouses.clear()
        sel = self.DB.selectAll()
        self.addressList = []
        for s in sel:
            self.addressList.append(s[1])
        self._ui.savedHouses.addItems(self.addressList)

    # calls all three graph methods
    def _setGraphs(self):
        self._graph1()
        self._graph2()
        self._graph3()

    # reads csv file and converts to a pandas data frame
    def _csvToPandas(self):
        self._X = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/MachineLearning/bostonWeights.csv"))
        self._Y = (pd.read_csv(
            "/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/MachineLearning/bostonTarget.csv"))

    # plot canvas for embedded scatter plot
    def _graph3(self):
        self._ui.widget_3.canvas.ax.set_facecolor((.84, .84, .84, 1))
        comboBoxText = self._ui.selectFeature.currentText()
        comboBoxIndex = self._ui.selectFeature.currentIndex()
        switcher = {0: 'CRIM', 1: 'AGE', 2: 'PTRATIO', 3: 'TAX', 4: 'RM'}
        self._ui.widget_3.canvas.ax.scatter(
            self._X[switcher[comboBoxIndex]], self._Y['0'] * 10000, color='black'
        )

        # if user has entered data, plot it on the graph with a different color
        if self._userHouseSpecs is not None:
            self._ui.widget_3.canvas.ax.scatter(
                self._userHouseSpecs[comboBoxIndex], self._userHouseSpecs[5], color='red', s=120, marker='o'
            )
        self._ui.widget_3.canvas.ax.set(title=comboBoxText, xLabel=comboBoxText)
        self._ui.widget_3.canvas.draw()

    # plot canvas for embedded bar graph
    def _graph2(self):
        self._ui.widget_2.canvas.ax.set_facecolor((.84, .84, .84, 1))
        self._ui.widget_2.canvas.ax.bar(self._barChartMap.keys(), self._barChartMap.values(), color='blue')
        self._ui.widget_2.canvas.ax.set(title="Statistics")
        self._ui.widget_2.canvas.draw()

    # plot canvas for embedded histogram
    def _graph1(self):
        self._ui.widget.canvas.ax.set_facecolor((.84, .84, .84, 1))
        self._ui.widget.canvas.ax.hist(self._Y['0'] * 10000, rwidth=0.6, color='green')
        self._ui.widget.canvas.ax.set(title="Prices Sold", xLabel="Prices Sold", yLabel="Volume")
        self._ui.widget.canvas.draw()

    # connects push buttons to handler methods
    def _actionHandling(self):
        # find and assign buttons
        self._ui.predict.clicked.connect(self._predictMethod)
        self._ui.selectFeature.activated.connect(self._selectFeatureMethod)
        self._ui.load.clicked.connect(self._loadMethod)
        self._ui.dele.clicked.connect(self._deleteMethod)
        # find and assign text fields
        self._houseAddress = self.findChild(QtWidgets.QLineEdit, "i0")

    # handler method for accessing the MachineLearning predict model
    def _predictMethod(self):

        # make a list of all number inputs
        numberIns = [self._ui.i1.text(),
                     self._ui.i2.text(), self._ui.i3.text(), self._ui.i4.text(), self._ui.i5.text(),
                     self._ui.i6.text(), self._ui.i7.text(), self._ui.i8.text(), self._ui.i9.text(),
                     self._ui.i10.text(), self._ui.i11.text(), self._ui.i12.text(), self._ui.i13.text()
                     ]

        # check to see if the first input field is blank
        if (self._ui.i0_2.text()) == '':
            messageBoxForIDInput()
            return

        # check to see if the rest of the input fields are only digits
        # (floating point too, so isdigit() func is not a valid solution)
        for userIn in numberIns:
            if inputNotValid(userIn):
                return

        # create a new house object with valid input text
        # cast the inputs to either a str or a float
        house = House(
            str(self._ui.i0_2.text()), float(self._ui.i1.text()),
            float(self._ui.i2.text()), float(self._ui.i3.text()),
            float(self._ui.i4.text()), float(self._ui.i5.text()),
            float(self._ui.i6.text()), float(self._ui.i7.text()),
            float(self._ui.i8.text()), float(self._ui.i9.text()),
            float(self._ui.i10.text()), float(self._ui.i11.text()),
            float(self._ui.i12.text()), float(self._ui.i13.text())
        )

        # call MachineLearning method in House object and then set the prediction output
        predictionFloat64 = house.getLinearPrediction()
        predictionFloat = "{:.2f}".format(predictionFloat64)
        self.DB.insert(house)
        self.savedHousesComboBox()
        self._ui.widget_2.canvas.ax.clear()
        self._ui.widget_3.canvas.ax.clear()
        self._barChartMap = {"Min Price Sold": 50000.00,
                             "Max Price Sold": 500000.00,
                             "Mean Price Sold": 225328.06,
                             "Predicted Price": float(predictionFloat)}
        self._ui.prediction.setText(str(predictionFloat))
        self._graph2()

        # gather the scatter plot for the user's house and reset the graph
        self._userHouseSpecs = [house.houseSpecs[0],
                                house.houseSpecs[6], house.houseSpecs[10],
                                house.houseSpecs[9], house.houseSpecs[5],
                                float(predictionFloat)
                                ]
        self._graph3()

    # switches the scatter plot to the selected feature
    def _selectFeatureMethod(self):
        self._ui.widget_3.canvas.ax.clear()
        self._graph3()

    # loads the data from the saved house in the database
    def _loadMethod(self):
        salesId = self._ui.savedHouses.currentText()
        if not (salesId == ''):
            house = self.DB.select(salesId)
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
            # call the predict method and the scatter plot for the loaded data to reset
            self._predictMethod()
            self._selectFeatureMethod()

    # handler method to delete a house from the houses table
    def _deleteMethod(self):
        salesId = self._ui.savedHouses.currentText()
        if not (salesId == ''):
            self.DB.delete(salesId)
            self.savedHousesComboBox()


# create app and window objects and then open app
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.setWindowTitle("Real Estate Price Estimator")
app.exec()
