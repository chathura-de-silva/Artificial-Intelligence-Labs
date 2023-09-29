## Assignment 1

A courier service is responsible for delivering packages within a busy city. Your task is to optimize the delivery routes. Here are the key points:

- Each package has a specific delivery address.
- Delivery trucks have limited capacities.
- The city map is represented as a graph with delivery locations as nodes and roads as edges.
- Travel time between two nodes is proportional to the distance between them on the map.
- The courier service station, represented as node "a," is the starting point.

## Assignment Overview

Task in this assignment is to:

1. Read an input file named "input.txt."
2. Parse the city map, number of trucks, and truck capacities from the input file.
3. Implement the Hill-Climbing algorithm to find the delivery sequence for each truck.
4. Write the results to an output file named "\<\<index number\>\>.txt."
5. Each line in the output file should show "truck_\<\<number>>#<<delivery sequence (comma separated)\>\>," followed by the total distance traveled by all trucks.

## Input Format

- The input file contains a city map as an n x n matrix.
- "N" indicates no road between nodes.
- The input file also contains information about the trucks in the format "truck_<<number>>#<<capacity>>."

## Output Format

- The output file will contain the delivery sequence for each truck and the total distance traveled by all trucks.

## Example Output

```plaintext
truck_1#b,c
truck_2#f,e,d
52
```
## Implementation Details 
*   Uncomment the print statements if there is any need to see the intermediate steps or to debug.
*   Change the number of iterations and rename the "output.txt" to whatever required accordingly by changing,
    ```python
    # Change below parameters accordingly.
    INDEX_NUMBER = 'output'
    ITERATIONS = 10000
    ```
    in the main.py.
## Greedy Assumption
*   The direct route between two destinations is the shortest root.
## Recommended Python version
*   Python 3.8