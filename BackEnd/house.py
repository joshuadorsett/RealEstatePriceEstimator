from MachineLearning.trainedModels import linearPricePrediction


class House:
    # constructor needs to receive all of the independent variables needed for MachineLearning models
    def __init__(self, SALESID, CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
        # house specs contains users arguments for the house
        self.salesId = SALESID
        self.houseSpecs = [CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]
        self.linearPrediction = None

    # this returns the prediction from the lin regression model and sets the linear prediction attribute.
    def getLinearPrediction(self):
        if self.linearPrediction is None:
            self.linearPrediction = linearPricePrediction([self.houseSpecs])
        return self.linearPrediction
