# main file to test all functions until PyQt5 takes over as the user interface.

from oopModels.House import House
from oopModels.User import User

user = User("james", "password")

print(user.getName(), " : ", user.getPassword())

house = House(.28, 0.00, 11.69, 0.00, .624, 6.623, 94.05, 0.07, 5, 370, 19, 391, 3)

prediction = house.getLinearPrediction()

print(prediction)
