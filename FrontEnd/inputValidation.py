# a group of util functions for checking inputs
from PyQt5.QtWidgets import QMessageBox


# this checks to see if a string can be cast to a float without error
def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


# this opens a message box concerning an invalid input
def messageBoxForInputs():
    msg = QMessageBox()
    msg.setWindowTitle("Invalid Inputs.")
    msg.setText("The inputs were invalid. Please enter valid digits in all fields.")
    msg.setStyleSheet("background-color: 'white';")
    msg.exec()


# this checks to see if the input is not blank and a float
def inputNotValid(text):
    if not (not (text == '') and (is_float(text))):
        messageBoxForInputs()
        return True
