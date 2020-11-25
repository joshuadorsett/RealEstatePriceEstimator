from PyQt5 import QtWidgets
import sys

from GUI.RealEstatePriceEstimator_ui import Ui_MainWindow

# use pyuic5 -o RealEstatePriceEstimator_ui.py RealEstatePriceEstimator.ui in the GUI folder every time you want to
# update ui design
# class for importing UI from QT Designer
from oopModels.House import House


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # call inherited constructor
        self._uiInit()
        self.show()  # Show the GUI

    def _uiInit(self):
        self.setFixedSize(1540, 1020)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._actionHandling()

    def _actionHandling(self):
        # find and assign buttons
        self.ui.save.clicked.connect(self._saveMethod)
        self.ui.load.clicked.connect(self._loadMethod)
        self.ui.dele.clicked.connect(self._deleteMethod)
        self.ui.predict.clicked.connect(self._predictMethod)

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
                      float(self.ui.i1.text()),
                      float(self.ui.i2.text()),
                      float(self.ui.i3.text()),
                      float(self.ui.i4.text()),
                      float(self.ui.i5.text()),
                      float(self.ui.i6.text()),
                      float(self.ui.i7.text()),
                      float(self.ui.i8.text()),
                      float(self.ui.i9.text()),
                      float(self.ui.i10.text()),
                      float(self.ui.i11.text()),
                      float(self.ui.i12.text()),
                      float(self.ui.i13.text())
                      )

        # call ML method in House object and then set the prediction into the GUI
        predictionFloat64 = house.getLinearPrediction()
        predictionFloat = "{:.2f}".format(predictionFloat64)
        self.ui.prediction.setText(str(predictionFloat))


# create app and window objects and then open GUI
app = QtWidgets.QApplication(sys.argv)  # Create an instance of app

window = Ui()  # create instance of Ui

app.exec()  # execute app
