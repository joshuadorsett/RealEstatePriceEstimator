# main file to test all functions until PyQt5 takes over as the user interface.
from pandas import DataFrame
import pandas as pd
from oopModels.House import House
from oopModels.User import User

user = User("james", "password")

print(user.getName(), " : ", user.getPassword())

house = House(.28, 0.00, 11.69, 0.00, .624, 6.623, 94.05, 0.07, 5, 370, 19, 391, 3)

prediction = house.getLinearPrediction()

print(prediction)

X = (pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonWeights.csv"))
Y = (pd.read_csv("/Users/joshuadorsett/PycharmProjects/RealEstatePriceEstimator/ML/bostonTarget.csv"))
X = X.loc[:,'AGE']

# print(X)

print(Y)