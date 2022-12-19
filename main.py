# The first part of the code is similar to the code found in the notes since we were allowed to use that code
import csv

# This part open the CSV file for it to be read
with open('prim-deliverable2.txt', 'r') as csv_file:
    file_handle = csv.reader(csv_file)
    data = next(file_handle)

# Reads the number of vertices
number_of_vertices = int(data[0])
# Starts the total edges at 0 to start counting
edge_total = 0
graph = [[0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
edges = []
k = 0

# Puts the matrix into something that can be analyzed
for i in range(0, number_of_vertices):
    for j in range(0, number_of_vertices):
        edge_total = edge_total + 1
        k += 1
        graph[i][j] = int(data[k])
        if int(data[k]) != 0:
            edges.append((int(data[k]),i,j))

# Sorts the edges based on the weight
edges.sort()

# These lists are appended to as we meet the conditions in algorithm below
components = []
spanning_tree = []
vertices = []

# First vertex appended as the 0 value
vertices.append(0)

# We have a vertex so we set the total vertices to 1
total_vertices = 1
# Weight starts at 0
total_weight = 0

# While loop goes until the total vertices is no longer less than
while (total_vertices < int(data[0])):
    # Starts off at 0
    i = 0
    # Used a while loop because you cannot restart a for loop but you can reset a while loop with a count
    # Loops until the length of the amount of edges in the matrix
    while i < (len(edges)):
        # Starts off at edges[i] and then iterates through the edges
        edge = edges[i]
        start_vertex = edge[1]
        end_vertex = edge[2]
        
        # Checks to see if a vertex already in the vertices array is present in the edge     
        if (start_vertex in vertices or end_vertex in vertices):
            # Checks to see if there is not a loop and that only vertex is present and not both
            if (not (start_vertex in vertices and end_vertex in vertices)):
                # Adds the weight of the current edge to the total weight
                total_weight = total_weight + edges[i][0]
                # Resets the i value whenever this condition is met to iterate through the edges again
                i = 0
                # Checks to see which vertex is new and to be added to the list of vertices
                if (not(end_vertex in vertices)):
                    vertices.append(end_vertex);
                if (not(start_vertex in vertices)):
                    vertices.append(start_vertex);
                # Adds the start vertex and the end vertex to the components
                components.append([start_vertex, end_vertex])
                # Adds the edge to the spanning tree to output later
                spanning_tree.append(edge);
                # Since condition was met we increase the vertices that we found by 1
                total_vertices = total_vertices + 1
        # If the edge is not able to be added then you move onto the next i value meaning next edge
        i = i + 1

# Outputs data to show the Prim's algorithm was done correctly
print("------------------------")
print("The total number of vertices is ", total_vertices)
print("The spanning tree contains these weighted edges:\n")                    
for edge in spanning_tree:
    print("Adding Edge (",edge[1],",",edge[2],") with weight",edge[0])
    
print("\nThe total weight is ", total_weight)
print("------------------------")