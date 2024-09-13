import numpy as np
def row_reduce(matrix):
    matrix = matrix.astype(float)  # Ensure we are working with floats for division
    rows, cols = matrix.shape

    for i in range(rows):
        # Make the diagonal element 1 by dividing the entire row
        pivot = matrix[i, i]
        if pivot == 0:
            # Swap with a row below to get a non-zero pivot, if possible
            for k in range(i + 1, rows):
                if matrix[k, i] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    pivot = matrix[i, i]
                    break
        if pivot != 0:
            matrix[i] = matrix[i] / pivot

        # Make all rows below this one 0 in the current column
        for j in range(i + 1, rows):
            if matrix[j, i] != 0:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

    # Back substitution to make the upper triangular matrix into a diagonal matrix
    for i in range(rows - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if matrix[j, i] != 0:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]

    return matrix

def get_minor(matrix,i,j):
    # returns the minor of a matrix
    def remove_row(matrix, i):
        matrix = np.array(matrix)
        if i < 0 or i >= matrix.shape[0]:
            raise IndexError("Row index out of bounds")
        return np.vstack((matrix[:i], matrix[i+1:]))
    def remove_column(matrix, j):
        matrix = np.array(matrix)
        if j < 0 or j >= matrix.shape[1]:
            raise IndexError("Column index out of bounds")
        return np.hstack((matrix[:, :j], matrix[:, j+1:]))
    output = remove_row(matrix,i)
    output = remove_column(output,j)
    return output

def determinant(matrix):
    """Recursively calculate the determinant of a matrix."""
    # Base case for 2x2 matrix
    rows, cols = matrix.shape
    if rows != cols:
        return "Matrix is not square, cannot get determinant"
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(get_minor(matrix, 0, c))
    return det



def matmult(matrix1, matrix2):
    r1, c1 = matrix1.shape
    r2, c2 = matrix2.shape
    if c1 != r2:
        return 'Matrices do not match, cannot get product'
    else:
        output = np.zeros((r1, c2))
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    output[i][j] += matrix1[i][k] * matrix2[k][j]
    return output

def gauss_jordan_inverse(A):
    n = len(A)
    I = np.eye(n)
    AI = np.hstack((A, I))
    
    for i in range(n):
        # Check for zero diagonal element
        if AI[i, i] == 0:
            # Find a row below to swap with
            for k in range(i+1, n):
                if AI[k, i] != 0:
                    AI[[i, k]] = AI[[k, i]]
                    break
            else:
                # No suitable row found; matrix is singular
                return None
        
        # Make the diagonal contain all 1s
        diag_element = AI[i, i]
        AI[i] = AI[i] / diag_element
        
        for j in range(n):
            if i != j:
                row_factor = AI[j, i]
                AI[j] = AI[j] - row_factor * AI[i]
    
    A_inv = AI[:, n:]
    return A_inv

def is_invertible_and_inverse(A):
    try:
        A_inv = gauss_jordan_inverse(A)
        if A_inv is None:
            return False, None
        return True, A_inv
    except Exception as e:
        return False, None
    
# # Define an augmented matrix [A|B]
# A = np.array([[1, 1, 1],
#               [0, 1, 2],
#               [2, 2, 0]], dtype=float)
# B = np.array([[16],
#               [21],
#               [16]], dtype=float)


# # Create the augmented matrix
# augmented_matrix = np.hstack((A, B)).astype(int)
# print("Original augmented matrix:\n", augmented_matrix)

# # Perform row reduction
# reduced_matrix = row_reduce(augmented_matrix).astype(int)
# print("Row reduced matrix:\n", reduced_matrix)



# A = np.array([[1,2],
#               [1,1]])
# B = np.array([[1,2],
#               [1,5]])
# C = matmult(A,B)
# print(C)
# C = A@B
# print(C)
# C = np.dot(A,B)
# print(C)
# C = np.outer(A,B)
# print(C)
# C = np.trace(A)

A = np.array([[-1,2,0],
              [ 4,5,3]])
B = np.array([[7,1,-3],
              [2,0,6]])
C = np.array([[1,2],
              [-4,9]])
D = np.array([[11,5],
              [0,-2]])
E = np.array([[0,1],
              [1,0],
              [0,3]])

A = np.array([[1,0],
              [-1,-2]])
B = np.array([[2,3,1],
              [3,1,2]])
C = np.array([[-1],[2],[2]])
D = np.array([[1,2,0],
              [0,1,2],
              [-1,3,4]])
E = np.array([[-3,2],
              [1,7]])

# print('CB:\n',C@B)
# print('EE:\n',E@E)
# # print('BB:\n',B@B)
# print('DC:\n',D@C)
# print('AB:\n',A@B)
# print('BA:\n',B@A)

A = np.array([[1,2,3],
              [1,0,-1]])
ATA = np.transpose(A)@A
# print(ATA)
# print(ATA[2][2])

A = np.array([[1,3,-3],
              [3,0, 5]])
B = np.array([[ 3,0],
              [-3,1],
              [ 0,5]])
# print(A@B)

M = np.array([[1,1,2,3,13],
              [1,-2,1,1,8],
              [3,1,1,-1,1]])
M_d = row_reduce(M)
# print(M_d)

a = 2
M = np.array([[1,1,-1,2],
              [1,2,1,3],
              [1,1,(a**2-5),a]])
M_d = row_reduce(M)
# print(M_d)

M = np.array([[1,1,2,3,13],
              [1,-2,1,1,8],
              [3,1,1,-1,1]])
M_d = row_reduce(M)
# print(M_d)
# print(M_d[1][4])



# Define a matrix
A = np.array([[6, 1],
              [3, 4]], dtype=float)
B = np.array([[8, 5, -8],
              [7, 2, -7],
              [-4, 0, 4]], dtype=float)
C = np.array([[2,1,3],
              [0,1,2],
              [1,0,3]])
# Check if the matrix is invertible and get the inverse
invertible, A_inv = is_invertible_and_inverse(C)

# if invertible:
#     print("The matrix is invertible. The inverse is:")
#     print(A_inv)
# else:
#     print("The matrix is not invertible.")

# D = np.array([[3,1,2],
#               [-3,-1,-6],
#               [6,5,3]])
# E = np.array([[2,-2,6,4],
#               [2,2,7,1],
#               [6,-6,13,14],
#               [-2,2,-6,1]])
# F = np.array([[5,2,-2,5,-4],
#               [0,4,2,1,0],
#               [0,0,-2,3,7],
#               [0,0,0,-1,-5],
#               [0,0,0,0,2]])
# G = np.array([[4,2,7],
#               [9,3,5],
#               [7,9,4]])
# H = np.array([[4,2,2,0],
#               [2,0,0,0],
#               [3,0,0,1],
#               [0,0,1,0]])

# print('D:',np.linalg.det(D))
# print('E:',np.linalg.det(E))
# print('F:',np.linalg.det(F))
# print('G:',np.linalg.det(G))
# print('H:',np.linalg.det(H))

# I = np.array([[-5,4],
#               [0,4]])
# invertible, A_inv = is_invertible_and_inverse(I)
# if invertible:
#     print("The matrix is invertible. The inverse is:")
#     print(A_inv)
# else:
#     print("The matrix is not invertible.")

A = np.array([[1, 0,1,2],
              [2,-1,1,3]])
A = np.array([[1,3,1,0],
              [2,5,0,1]])
print(row_reduce(A))
A=np.array([[9,3],
            [4,-5]])
B=np.array([[5],
            [-2]])
print(A@B)