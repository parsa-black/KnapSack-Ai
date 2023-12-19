# Import Dependencies
# from random import randint
from random import shuffle
import csv

# Specify the path to your CSV file
csv_file_path = './KnapSack.csv'

# Set The Problem  and Algorithm parameters
N = 29  # Number of items
MAX_WEIGHT = 220  # Maximum Weight of Bag
MAX_SIZE = 2  # Maximum Size of Bag
objects = []

POPULATION_SIZE = 5
MUTATION_RATE = 0.8
EPOCH = 200


# Item Class
class Item:
    def __init__(self, item_weight, item_size, item_value):
        self.weight = item_weight
        self.size = item_size
        self.value = item_value


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
def init_population(n, p):
    population_list = []
    for i in range(p):
        new_member = [0 for i in range(n)] + [1 for i in range(n)]
        shuffle(new_member)
        new_member = new_member[:n] + [None, None, None]  # Weight, Size, Value
        population_list.append(new_member)
    return population_list


# Cross Over Function
def cross_over(population_list, n, p):
    n_new = n//2
    for i in range(0, p, 2):
        child1 = population_list[i][:n_new] + population_list[i+1][n_new:] + [None, None]
        child2 = population_list[i+1][:n_new] + population_list[i][n_new:] + [None, None]
        population_list.append(child1)
        population_list.append(child2)
    return population_list


# Main
if __name__ == "__main__":
    print(f"MAX WEIGHT: {MAX_WEIGHT}")
    print(f"MAX SIZE: {MAX_SIZE}")
    print("--------------------------------------")
    current_population = init_population(N, POPULATION_SIZE)
    current_population = cross_over(current_population, N, POPULATION_SIZE)
    for i in current_population:
        print(i)
