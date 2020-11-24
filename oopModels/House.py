import os

import joblib


class House:
    # constructor needs to receive all of the independent variables need for ML model
    # constructor automatically calls the machine learning model's prediction and returns answer
    # to attributes
    # finally, the constructor then automatically stores the features and the target into database of users account
    def __init__(self, CRIM, ZN, INDUS,	CHAS, NOX, RM, AGE,	DIS, RAD, TAX, PTRATIO, B, LSTAT):
        # house specs contains users arguments for the house
        self.houseSpecs = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
        folder = './joblib_memmap'
        try:
            os.mkdir(folder)
        except FileExistsError:
            pass
        model_filename = '/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/HousePricePrediction.joblib'
        model = joblib.load(model_filename)
        self.prediction = model.predict(self.houseSpecs)

    # this returns the prediction attribute in dollar amount
    def getPrediction(self):
        return self.prediction[0][0] * 10000

    # add house specs and prediction to data base with user ID
    def save(self):
        pass
