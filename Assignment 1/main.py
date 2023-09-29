import random
import copy


def destination_divider(destinations, solution):
    random.shuffle(destinations)
    solution_copy = copy.deepcopy(solution)
    destinations_copy = destinations.copy()
    for _truck in solution_copy:
        _truck.append(destinations_copy[:_truck[1]])
        destinations_copy = destinations_copy[_truck[1]:]
    return solution_copy


def distance_counter(destination_sequence):
    global graph
    distance = 0
    current_location = 0
    for destination in destination_sequence:
        distance += graph[current_location][destination]
        current_location = destination
    return distance


try:
    with open("input.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
        print("input_data  :", input_data)
except IOError:
    print("Error occurred while reading the input.txt!")

n = len(input_data[0].split(","))
graph = []

for i in range(n):
    line = input_data[0]
    graph.append([int(x) if x.isnumeric() else float('inf') for x in line.split(",")])
    input_data.pop(0)

print("graph :",graph)
trucks = []
for truck_data in input_data:
    trucks.append([int(x) if x.isnumeric() else x for x in truck_data.split("#")])
print("Trucks :", trucks)

destination_list = [x for x in range(1, n)]
best_solution = []
best_distance = float("inf")
for i in range(10000):
    current_solution = destination_divider(destination_list, trucks)
    total_distance = 0
    for truck in current_solution:
        total_distance += distance_counter(truck[-1])
    if total_distance < best_distance:
        best_distance = total_distance
        best_solution = current_solution
        # print("solution :", [x[-1] for x in current_solution], "distance : ", total_distance)
print("Final answer :", best_solution, best_distance)
