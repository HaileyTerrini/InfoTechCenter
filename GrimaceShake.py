print("***************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
        gasLevelList = ["Empty","Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
        currentGasLevel = random.choice(gasLevelList)
        return currentGasLevel

#Function that lists Gas Stations, m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K", "Moble", "Costco", "Meijer", "7Eleven"]
    gasStationsNearby = random.choice (gasStations)
    return gasStationsNearby

#Function will call the gasLecelGauge to detirmine out gas lave; and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
         print("***WARNING - YOU ARE ON EMPTY***\n")
            sleep(2.5)
         print("   ***Calling Triple AAA***")
    elif gasLevelIndicator =="Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsLow,"miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking google maps for the closest gas stations...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(), "which is",milesToGasStationsQuarterTank,"miles away")
    elif gasLevelIndicator == "Half Tank":
        print("Your has tank is a half of a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank"
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full - YEAHH!!! - Congratulations! - Vroom Vrooms!")




gasLevelAlert()