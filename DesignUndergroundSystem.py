class UndergroundSystem:

    def __init__(self):
        self.passDict = {}
        self.distDict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.passDict:
            self.passDict[id] = (stationName, t)
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.passDict:
            origin, time = self.passDict[id]
            # If the originating station already exists in the dictionary
            if origin in self.distDict:
                # If a trip has already been made from origin to destination
                if stationName in self.distDict[origin]:
                    self.distDict[origin][stationName][0] += (t - time)
                    self.distDict[origin][stationName][1] += 1
                # If this is the first time this trip has been made
                else:
                    self.distDict[origin][stationName] = [t-time, 1]
            else:
                self.distDict[origin] = {stationName: [t-time, 1]}
            # Remove the passenger from the passenger dictionary
            self.passDict.pop(id)
        return


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, trips = self.distDict[startStation][endStation]
        return float(time)/trips


if __name__ == '__main__':
    commands = ["checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    params = [[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

    train = UndergroundSystem()

    for i in range(len(commands)):
        if commands[i] == "checkIn":
            print(train.checkIn(params[i][0], params[i][1], params[i][2]))
        elif commands[i] == "checkOut":
            print(train.checkOut(params[i][0], params[i][1], params[i][2]))
        else:
            print(train.getAverageTime(params[i][0], params[i][1]))


"""
Use a dict to keep track of where each passenger is checked in and when they
checked in:
    {42: ("Waterloo", 3),
     33: ("Paradise, 12)
     }
When a passenger is checking in make sure they aren't already checked in 
somewhere.
When checking out, determine the time it took to travel from origin to
destination and update the Distance Dictionary. Then remove that passenger from
the Passenger dictionary.

Distance Dictionary structure:
    {"Origin1": {"Destination1": [total time from trips, # of trips],
                 "Destination2": [total time from trips, # of trips]},
     "Origin2": {"Destination1": [total time from trips, # of trips],
                 "Destination2": [total time from trips, # of trips]}
    }
"""