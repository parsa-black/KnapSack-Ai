# Import Dependencies
from random import randint
from random import shuffle

# Set The Problem  and Algorithm parameters
N = 29  # Number of items
MAX_WEIGHT = 220  # Maximum Weight of Bag
objects = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]

POPULATION_SIZE = 4
MUTATION_RATE = 0.8
EPOCH = 200


# Item Class

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


# Item Getter Function

def get_items(n, input_items=None, verbos=0):
    items = []
    if input_items is None:
        for i in range(n):
            print(f"Items #{i + 1}")
            item_value = int(input("Please Enter the Value of The Item: "))
            item_weight = int(input("Please Enter the Weight of The Item: "))
            items.append(Item(item_value, item_weight))
    else:
        for item in input_items:
            items.append(Item(item[0], item[1]))
    if verbos:
        for item in items:
            print(f"Item #{items.index(item) + 1}: Value:{item.value} Weight:{item.weight}")
    return items


# Main
if __name__ == "__main__":
    print(f"MAX WEIGHT: {MAX_WEIGHT}")
    print("--------------------------------------")
    items = get_items(N, input_items=objects, verbos=1)
    print("--------------------------------------")

