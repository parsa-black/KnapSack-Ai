# Import Dependencies
from random import randint
from random import shuffle
import csv

# Specify the path to your CSV file
csv_file_path = './KnapSack.csv'

# Set The Problem  and Algorithm parameters
N = 20  # Number of items
MAX_WEIGHT = 220  # Maximum Weight of Bag
MAX_SIZE = 2  # Maximum Size of Bag
objects = []

POPULATION_SIZE = 300
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
    # Print items
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
        child1 = population_list[i][:n_new] + population_list[i+1][n_new:]
        child2 = population_list[i+1][:n_new] + population_list[i][n_new:]
        population_list.append(child1)
        population_list.append(child2)
    return population_list


# Mutation Function
def mutation(population_list, n, p, m):

    chosen_ones = [i for i in range(p, p*2)]
    shuffle(chosen_ones)
    chosen_ones = chosen_ones[:int(((p*2)-1)*m)]
    for i in chosen_ones:
        cell = randint(0, n-1)
        population_list[i][cell] = 1 if population_list[i][cell] == 0 else 0
    return population_list


# Fitness Function
# Weight
def weight_distance(bag, n, max_weight, items_list):
    total_weight = 0
    list_weight = 0
    for i in range(n):
        if bag[i]:
            total_weight += int(items_list[i].weight)
    if total_weight <= max_weight:
        list_weight = abs(total_weight - max_weight)
    else:
        list_weight = 500
    return list_weight


# Size
def size_distance(bag, n, max_size, items_list):
    total_size = 0
    list_size = 0
    for i in range(n):
        if bag[i]:
            total_size += float(items_list[i].size)
    if total_size <= max_size:
        list_size = abs(total_size - max_size)
    else:
        list_size = 10.00
    return round(list_size, 2)


# Value
def value(bag, n, items_list):
    total_value = 0
    for i in range(n):
        if bag[i]:
            total_value += int(items_list[i].value)
    return total_value


# Fitness
def fitness(population_list, n, p, items_list, max_weight, max_size):
    for i in range(p*2):
        population_list[i][n] = weight_distance(population_list[i], n, max_weight, items_list)
        population_list[i][n+1] = size_distance(population_list[i], n, max_size, items_list)
        population_list[i][n+2] = value(population_list[i], n, items_list)
    return population_list


# Sorter
def sorter(population_list, index1, index2, index3):
    if index1 == 500:
        pass
    elif index2 == 10.0:
        pass
    else:
        sorted_list = sorted(population_list, key=lambda x: (x[index1], x[index2], -x[index3]))
        return sorted_list


# Main
if __name__ == "__main__":
    loop = 1
    print(f"MAX WEIGHT: {MAX_WEIGHT}")
    print(f"MAX SIZE: {MAX_SIZE}")
    print("--------------------------------------")
    current_population = init_population(N, POPULATION_SIZE)
    while loop:
        while EPOCH:
            current_population = cross_over(current_population, N, POPULATION_SIZE)
            current_population = mutation(current_population, N, POPULATION_SIZE, MUTATION_RATE)
            current_population = fitness(current_population, N, POPULATION_SIZE, objects, MAX_WEIGHT, MAX_SIZE)
            current_population = sorter(current_population, N, N + 1, N + 2)
            current_population = current_population[:POPULATION_SIZE]
            EPOCH -= 1
        else:
            if current_population[0][N] == 500:
                EPOCH = 200
            elif current_population[0][N + 1] == 10.0:
                EPOCH = 200
            else:
                loop = 0
                print("Best Found Solution:", current_population[0])
