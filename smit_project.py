import numpy as np

TOTAL_X_NODES = 21          #this are the tottale nnumber of nodes in the x direction
TOTAL_Y_NODES = 41          #this are the tottale nnumber of nodes in the y direction
TOLERANCE = 0.01            #this is the allowed error in the calculations
NODE_SPACING = 0.05         #this is the physical spacing between any two nodes in the square plate

# initializing the temperature matrix to zero
TEMP_MATRIX = np.zeros(TOTAL_X_NODES * TOTAL_Y_NODES, dtype="float64").reshape(TOTAL_X_NODES, TOTAL_Y_NODES)

# Setting the boundary conditions
TEMP_MATRIX[...][0] = 100                   #surface y=0, other are 0 by default
TEMP_MATRIX[...,0] = 0                      #surface x=0
TEMP_MATRIX[...][TOTAL_Y_NODES] = 100       #surface y=2,
TEMP_MATRIX[...,TOTAL_X_NODES] = 0          #surface x=z



# initializing error to 1 (which is random value grater than TOLERANCE)
error = 1

while error > TOLERANCE:
    TEMP_MATRIX_NEXT = np.zeros(TOTAL_X_NODES * TOTAL_Y_NODES, dtype="float64").reshape(TOTAL_X_NODES, TOTAL_Y_NODES)
    TEMP_MATRIX_NEXT[...][0] = 100       #surface y=0, other are 0 by default

    for x in range(1, TOTAL_X_NODES - 1):
        for y in range(1, TOTAL_Y_NODES - 1):
            TEMP_MATRIX_NEXT[x][y] = (TEMP_MATRIX[x+1][y] + TEMP_MATRIX[x-1][y] + TEMP_MATRIX[x][y+1] + TEMP_MATRIX[x][y-1]) / 4

    #calculating the error of the iteration
    error = abs(TEMP_MATRIX_NEXT - TEMP_MATRIX).max()

    #setting the TEMP_MATRIX to the newly iterated matrix
    TEMP_MATRIX = TEMP_MATRIX_NEXT

np.savetxt("temp_matrix.csv", TEMP_MATRIX, delimiter=",")
