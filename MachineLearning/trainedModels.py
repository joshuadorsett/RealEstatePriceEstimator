import joblib


#  calls the saved joblib file for the lin regression model
def linearPricePrediction(featuresList):
    model_filename = \
        '/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator' \
        '/MachineLearning/HousePricePrediction.joblib'
    linRegModel = joblib.load(model_filename)
    return linRegModel.predict(featuresList)[0][0] * 10000
