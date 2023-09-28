try:
    with open("input.txt", "r") as input_file:
        input_data = [line.strip() for line in input_file.readlines()]
        # print(input_data)
except IOError:
    print("Error occurred while reading the input.txt!")

n = len(input_data[0].split(","))
graph = []

i = 0
while i < n:
    graph.append(input_data[0].split(","))
    input_data.pop(0)
    i += 1
# print(graph)
trucks = {}
distance = 0
for truck_data in input_data:
    truck_name, capacity = truck_data.split("#")
    trucks[truck_name] = capacity
