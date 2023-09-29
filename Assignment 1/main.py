import random


def destination_divider(destinations):
    global trucks
    random.shuffle(destinations)
    print(destinations)
    for truck in trucks:
        truck.append(destinations[:truck[1]])
        destinations = destinations[truck[1]:]


try:
    with open("input.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
        # print(input_data)
except IOError:
    print("Error occurred while reading the input.txt!")

n = len(input_data[0].split(","))
graph = []

for i in range(n):
    line = input_data[0]
    graph.append([int(x) if x.isnumeric() else float('inf') for x in line.split(",")])
    input_data.pop(0)

print(graph)
trucks = []
distance = 0
for truck_data in input_data:
    trucks.append([int(x) if x.isnumeric() else x for x in truck_data.split("#")])
print(trucks)

destination_list = [x for x in range(1, n)]
best_routes = []
best_distance = float('inf')

destination_divider(destination_list)
print(trucks)
