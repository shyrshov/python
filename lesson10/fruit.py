from enum import Enum
from functools import reduce


# 1) Enum Definition:
# Define an Enum named "Fruit" with values: Apple, Banana, Orange, Grape, Strawberry.

class Fruit(Enum):
   APPLE = 10
   BANANA = 20
   ORANGE = 30
   GRAPE = 40
   STRAWBERY = 50

# 2) Filter Fruits:
# Create a list of fruits containing duplicate entries.
# Write a function named "filter_duplicate_fruits" that takes a list of fruits and uses the filter function to remove duplicate entries.Print the filtered list of fruits.

list_of_fruits = [Fruit.APPLE, Fruit.BANANA, Fruit.ORANGE, Fruit.APPLE]

def filter_duplicate_fruits(l):
   in_list = []
   return list(filter(lambda x: in_list.append(x) is None if x not in in_list else False, l))

print(filter_duplicate_fruits(list_of_fruits))

# 3) Map Prices:
# Create a dictionary that maps each fruit (from the "Fruit" Enum) to its respective price.
# Write a function named "apply_discount" that takes the fruit-price dictionary and applies a 10% discount to each fruit's price using the map function.Print the updated fruit-price dictionary.

fruits_dict = {f.name: f.value for f in Fruit}
print(fruits_dict)


def apply_discount(dictionary, discount = 10):
    return dict(map(lambda f: (f[0], f[1] * (1 - discount / 100)), dictionary.items()))

fruits_with_discount = apply_discount(fruits_dict, 20)
print(fruits_with_discount)

# 4) Reduce Total Price:
# Use the same fruit-price dictionary from the previous task.
# Write a function named "calculate_total_price" that uses the reduce function to calculate the total price of all the fruits after the discount.
# Print the total price.

def calculate_total_price(dictionary):
   return reduce(lambda x, y: x + y, dictionary.values())

print(calculate_total_price(fruits_with_discount))

# 5) Check All and Any:
# Create a list of fruits.
# Write a function named "check_fruit_conditions" that checks if all fruits have names starting with the same letter and if any fruit name contains the letter "a", using the all and any functions.
# Print the results of both checks.

list_of_fruits = [f.name for f in Fruit]
print(list_of_fruits)

def check_fruit_conditions(list):
    first_letter = list[0][0]
    return all(f[0] == first_letter for f in list) & any('a' in f for f in list)

print(check_fruit_conditions(list_of_fruits))

# 6) Enum Utilization:
# Using the "Fruit" Enum, create a function that takes a fruit name as input 
# and returns a message saying whether the fruit is available or not.

def is_fruit_available():
   fruit = input('Type the fruit you want to check: ')
   if any(f.name == fruit for f in Fruit):
      return (f'Fruit {fruit} is available')
   else:
      return (f'Fruit {fruit} is not available')
   
print(is_fruit_available())