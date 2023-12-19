# Import Dependencies
from random import randint
from random import shuffle
import csv

# Specify the path to your CSV file
csv_file_path = './KnapSack.csv'

# Set The Problem  and Algorithm parameters
N = 1  # Number of items
MAX_WEIGHT = 220  # Maximum Weight of Bag
MAX_SIZE = 2  # Maximum Size of Bag
objects = []

POPULATION_SIZE = 29
MUTATION_RATE = 0.8
EPOCH = 200


# Item Class
class Item:
    def __init__(self, weight, size, value):
        self.weight = weight
        self.size = size
        self.value = value


with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    for row in csv_reader:
        weight = row[0]
        size = row[1]
        value = row[2]
        objects.append(Item(weight, size, value))
    objects.pop(0)
    # for i in range(29):
    #     print(f"item:{i} Weight: {objects[i].weight} Size:{objects[i].size} Value:{objects[i].value}")


# Init Population Function
def init_population(p):
    population_list = []
    for i in range(p):
        new_member = [0 for i in range(1)] + [1 for i in range(1)]
        shuffle(new_member)
        new_member = new_member[:1] + [objects[i].weight, objects[i].size, objects[i].value]  # Weight, Size, Value
        population_list.append(new_member)
    return population_list


# Main
if __name__ == "__main__":
    print(f"MAX WEIGHT: {MAX_WEIGHT}")
    print(f"MAX SIZE: {MAX_SIZE}")
    print("--------------------------------------")
    current_population = init_population(POPULATION_SIZE)
    for i in current_population:
        print(i)
