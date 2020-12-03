from PyQt5.QtWidgets import QMessageBox


# checks to see if a string can be cast to a float without error
def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


# creates a standard message box that receives a message.
def messageBox(message, title):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStyleSheet("background-color: 'white'; color: 'black';")
    msg.exec()


# opens a message box concerning an invalid digit input
def messageBoxForInputs(text):
    if text == '':
        text = "Leaving a field blank"
    digitError = text + " is an invalid entry. Please enter a valid digit."
    messageBox(digitError, "Invalid Input.")


# this checks to see if the input is not blank and a float
def inputNotValid(text):
    if not (not (text == '') and (is_float(text))):
        messageBoxForInputs(text)
        return True


# opens a message box concerning the first input field which does not have to be a digit
def messageBoxForIDInput():
    blankError = "The Sales Identifier was left blank. Please enter a unique name for the house."
    messageBox(blankError, "Invalid Input.")
