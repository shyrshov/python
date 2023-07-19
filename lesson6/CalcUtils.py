# Create utility class with name CalcUtils with the following static methods:
#     def calculateAverage(*args) # returns average of the given numbers as arguments
#     def filterPositives(lst: list) # returns filtered list of numbers > 0
#     def percent(number, percent) # return a percent of the given number

from statistics import mean

class CalcUtils:

    @staticmethod
    def calculateAverage(*args):
        return mean(args)
    
    @staticmethod
    def filterPositives(lst: list):
        return list(x for x in lst if x > 0)
    
    @staticmethod
    def percent(number, percent):
        return number * percent /100
    
print(CalcUtils.calculateAverage(1,5,15,2))
print(CalcUtils.filterPositives([1,5,15,0]))
print(CalcUtils.percent(100, 20))