import random
import copy
from itertools import permutations as perm
import sys

"""Change below parameters accordingly. ITERATIONS is the number of times the hill climbing algorithm is repeatedly 
applied to maximize the possibility of reaching the global minimum."""
INDEX_NUMBER = 'output'
ITERATIONS = 2000

"""destination_divider() function divides the destinations into trucks randomly then returns the probable solution by 
assigning travelling routes to each truck. Note that every destination that visited by truck may not be a delivery 
destination."""


def destination_divider(destinations, solution):
    """'is_delivered' and '_i' keeps track of the destinations that are already delivered. This handles when a truck
    goes through a destination that is already delivered so no need of delivery there. Slot in the truck will only
    get filled(i.e. '_i' getting incremented) whenever the destination is not delivered at the moment."""
    is_delivered = [False] * len(destinations)
    # Changing only a copy of the solution since we want to repeatedly apply hill climbing.
    solution_copy = copy.deepcopy(solution)
    for _truck in solution_copy:
        destinations_copy = destinations.copy()
        truck_capacity = _truck[1]  # Capacity of the truck is at index 1 of the truck list.
        current_location = 0  # Starting point is 0.
        # Initiating the route destination list with starting destination which is 0.      
        _truck.append([current_location])
        """"_i"Keeps track of the number of destinations in the truck.(Also could be interpreted as the number of 
        delivery items in the truck)"""
        _i = 0
        while _i < truck_capacity:
            random_destination = random.choice(destinations_copy)
            """Avoiding unnecessary duplication of visiting the same node already in being in it. Even without this 
            line the algorithm should work technically, but may require higher number of iterations to reach the same 
            accuracy."""
            if current_location != random_destination:
                _truck[2].append(random_destination)
                # Note that always the index of the destination is 1 less than the destination number.
                if is_delivered[random_destination - 1]:
                    _i -= 1
                else:
                    is_delivered[random_destination - 1] = True
                _i += 1
                """Remove method removes only the first occurrence. But here it is used without an ambiguity since we 
                are sure that any destination is not being repeated in the list."""
                destinations_copy.remove(
                    random_destination)
                # print("truck :", truck) # Uncomment for debugging purposes
    return solution_copy


# distance_counter() function takes a sequence of destinations and returns the total distance of the path sequence.
def distance_counter(destination_sequence):  # This is the objective function
    global graph
    distance = 0
    current_location = 0
    for destination in destination_sequence:
        distance += graph[current_location][destination]
        current_location = destination
    return distance


def hill_climbing(_initial_solution):
    # print("Initial solution at start of hill climbing :", _initial_solution) # Uncomment for debugging purposes
    optimal_distance = 0
    for _truck in _initial_solution:
        """_local_optimum_distance - Initializing the local optimum distance to infinity. This value is calculated 
        per truck. Not the total distance of the solution."""
        _local_optimum_distance = float('inf') 
        """This is the list of permutations of the destinations of each truck. Note that the starting point is
        removed since it is always 0."""
        route_permutation_list = list(
            perm(_truck[-1][1:]))  
        # To limit the computation time, only 1000 random permutations are considered.
        if len(route_permutation_list) > 1000:
            random.shuffle(route_permutation_list)
            route_permutation_list = route_permutation_list[-1000:]
        for route in route_permutation_list:
            # Adding the starting point to the route since earlier it was removed.
            current_route = [0] + list(route)
            current_distance = distance_counter(current_route)
            if current_distance < _local_optimum_distance:
                _local_optimum_distance = current_distance
                """Updating the route of the truck to the current route. This is actually changing the corresponding 
                trucks route inside the '_initial_solution'."""
                _truck[-1] = current_route
        # Adding the local optimum distance of each truck to get the total distance of the solution.
        optimal_distance += _local_optimum_distance
    # print("Initial solution,distance at end of hill climbing :", _initial_solution, optimal_distance) # Uncomment for
    # debugging purposes
    return _initial_solution, optimal_distance


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
    for i in range(
            ITERATIONS):  # Repeatedly applying the algorithm for ITERATIONS times to maximize the possibility of
        # reaching the global minimum.
        initial_solution = destination_divider(destination_list,
                                               trucks)  # Randomly dividing the destinations into trucks and
        # assigning travelling routes to each truck.
        local_optimum_solution, total_distance = hill_climbing(
            initial_solution)  # Applying hill climbing algorithm to the current initial solution and getting the
        # local optimum solution.

        if total_distance < best_distance:  # If the current solution is better than the best solution, update the
            # best solution.
            best_distance = total_distance
            best_solution = local_optimum_solution
            # print("solution :", [x[-1] for x in local_optimum_solution], "distance : ", total_distance)# Uncomment
            # above line for debugging purposes
    for truck in best_solution:
        truck[-1].pop(0)  # Removing the starting point from the route of each truck since its not expected in the final solution.
        truck[-1] = [chr(x + 97) for x in truck[-1]]  # Converting the destinations to their corresponding letters
    # print("Final answer :", best_solution, best_distance) # Uncomment for debugging purposes

    try:
        with open(f"{INDEX_NUMBER}.txt", "w") as output_file:  # Writing the output to the file
            # Below lines writes the output in the required format.
            output_file.writelines(truck[0] + "#" + (",".join(truck[-1])) + "\n" for truck in best_solution)
            output_file.write(str(best_distance))
    except IOError:
        print(f"Error occurred while writing to the {INDEX_NUMBER}.txt!")
        sys.exit(1)
except IOError:
    print("Error occurred while reading the input.txt!")
    sys.exit(1)
