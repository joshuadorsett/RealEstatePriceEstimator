import joblib


def linearPricePrediction( featuresList ):
    model_filename = '/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/HousePricePrediction.joblib'
    linRegModel = joblib.load(model_filename)
    return linRegModel.predict( featuresList )[0][0] * 10000
