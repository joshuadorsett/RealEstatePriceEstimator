import joblib


class House:
    # constructor needs to receive all of the independent variables need for ML model
    # constructor automatically calls the machine learning model's prediction and returns answer
    # to attributes
    # finally, the constructor then automatically stores the features and the target into database of users account
    def __init__(self):
        # house specs contains users arguments for the house
        self.houseSpecs = [[]]
        model = joblib.load('RealEstatePriceEstimator/ML/HousePricePrediction.joblib')
        self.prediction = model.predict(self.houseSpecs)

    # this returns the prediction attribute
    def returnPrediction(self):
        return self.prediction
