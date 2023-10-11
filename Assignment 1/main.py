import random
import copy

# Change below parameters accordingly.
INDEX_NUMBER = 'output'
ITERATIONS = 10000

"""destination_divider() function divides the destinations into trucks randomly then returns the probable solution.
Note that this doesn't change the outer scope variables "trucks list" and only change to the "destinations-list"
is randomising it."""


def destination_divider(destinations, solution):
    is_delivered = [False]*len(destinations)
    solution_copy = copy.deepcopy(solution)
    destinations_copy = destinations.copy()
    for truck in solution_copy:
        truck_capacity = truck[1]
        current_location = 0
        truck.append([current_location]) # This initiates the route destination list with starting destination which is 0.
        
        i=0
        while i < truck_capacity:
            random_destination = random.choice(destinations_copy)
            if current_location != random_destination: #Avoiding unnessacary duplication of visiting the same node already in being in it. Even without this line the algorithm should work technically.
                truck[2].append(random_destination)
                if is_delivered[random_destination-1]:
                    i-=1
                else:
                    is_delivered[random_destination-1] = True
                i+=1
                destinations_copy.remove(random_destination) #Remove method removes only the first occurance. But here it is used without an ambiguity since we are sure that any destination is not being repeated in the list.
    return solution_copy


"""
distance_counter() function takes a sequence of destinations and returns the total distance of the path. 
"""


def distance_counter(destination_sequence):
    global graph
    distance = 0
    current_location = 0
    for destination in destination_sequence:
        distance += graph[current_location][destination]
        current_location = destination
    return distance


try:
    with open("input.txt", "r") as input_file:  # Reading the input file
        input_data = [line.strip() for line in input_file.readlines()]
        # print("input_data  :", input_data) # Uncomment for debugging purposes

    n = len(input_data[0].split(","))  # Number of destinations including starting point
    graph = []

    for i in range(n):
        line = input_data[0]  # Reading the first line of the input file
        graph.append([int(x) if x.isnumeric() else float('inf') for x in line.split(",")])
        input_data.pop(0)  # Removing the first line of the input file

    # print("graph :", graph) # Uncomment for debugging purposes
    trucks = []
    for truck_data in input_data:
        trucks.append([int(x) if x.isnumeric() else x for x in truck_data.split("#")])
    # print("Trucks :", trucks) # Uncomment for debugging purposes

    destination_list = [x for x in range(1, n)]  # List of destinations excluding starting point
    best_solution = []
    best_distance = float("inf")
    for i in range(ITERATIONS):
        current_solution = destination_divider(destination_list, trucks)  # Randomly dividing the destinations into
        # trucks
        total_distance = 0
        for truck in current_solution:
            total_distance += distance_counter(truck[-1])
        if total_distance < best_distance:  # If the current solution is better than the best solution, update the best
            # solution
            best_distance = total_distance
            best_solution = current_solution
            # print("solution :", [x[-1] for x in current_solution], "distance : ", total_distance)
            # Uncomment above line for debugging purposes
    for truck in best_solution:
        truck[-1] = [chr(x + 97) for x in truck[-1]]  # Converting the destinations to their corresponding letters
    # print("Final answer :", best_solution, best_distance) # Uncomment for debugging purposes

    try:
        with open(f"{INDEX_NUMBER}.txt", "w") as output_file:  # Writing the output to the file
            # Below line writes the output in the required format.
            output_file.writelines(truck[0] + "#" + (",".join(truck[-1])) + "\n" for truck in best_solution)
            output_file.write(str(best_distance))
    except IOError:
        print(f"Error occurred while writing to the {INDEX_NUMBER}.txt!")
except IOError:
    print("Error occurred while reading the input.txt!")
