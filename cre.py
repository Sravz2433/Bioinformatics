
def create_matrix(size):
    # Initialize a matrix of given size with all elements as 1
    matrix = [[1 for _ in range(size)] for _ in range(size)]
    
    # Set the diagonal elements to -3
    for i in range(size):
        matrix[i][i] = -3
    
    return matrix

# Example usage
size = 20  # Size of the matrix
matrix = create_matrix(size)

# Print the matrix to verify
for row in matrix:
    print(row)