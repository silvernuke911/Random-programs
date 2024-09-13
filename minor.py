import numpy as np

A = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,1,2,3],
              [4,5,6,8]])

B = np.array([[3,0,2],
              [2,0,-2],
              [0,1,1]])

D = np.array([[3],
              [5],
              [7]])

E = np.array([[0],
              [0],
              [0]])

def get_minor(matrix,i,j):
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
    rows, cols = matrix.shape
    if rows != cols:
        raise IndexError("Non-square matrix, cannot get determinant") 
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(get_minor(matrix, 0, c))
    return det

def matrix_of_minors(matrix):
    rows,cols=matrix.shape
    output = np.zeros_like(matrix)
    for i in range(rows):
        for j in range(cols):
            output[i][j]=determinant(get_minor(matrix,i,j))
    return output

def cofactor_matrix(matrix):
    rows,cols=matrix.shape
    output = np.zeros_like(matrix)
    for i in range(rows):
        for j in range(cols):
            output[i][j]=(-1)**((i+1)+(j+1))*matrix[i][j]
    return output

def transpose(matrix):
    rows,cols = matrix.shape
    output = np.zeros([cols,rows])
    for i in range(rows):
        for j in range(cols):
            output[i][j]=matrix[j][i]
    return output

def cofactor_inverse(matrix):
    rows,cols=matrix.shape
    if rows!=cols:
        raise IndexError("Non-square matrix, cannot get inverse") 
    if determinant(matrix) == 0:
        raise IndexError("Matrix is singular, cannot get inverse")
    inv_det = 1/determinant(matrix)
    output = matrix_of_minors(matrix)
    output = cofactor_matrix(output)
    output = transpose(output)
    output = inv_det * output
    return output

def row_reduce(matrix):
    matrix = matrix.astype(float)
    n = len(matrix)
    for i in range(n):
        if matrix[i][i]==0:
            for k in range(i+1,n):
                if matrix[k][i]!=0:
                    matrix[[i,k]]=matrix[[k,i]]
                    break
            else:
                raise IndexError("Matrix is singular, cannot row reduce")
        diag_element=matrix[i][i]
        matrix[i]=matrix[i] / diag_element
        for j in range(n):
            if j != i:
                row_factor = matrix[j][i]
                matrix[j] = matrix[j] - row_factor * matrix[i]
        print(matrix)
    return matrix
def row_reduce1(matrix):
    matrix = matrix.astype(float)
    n, m = matrix.shape
    
    # Loop through each row
    for i in range(n):
        if np.all(matrix[i] == 0):  # Check if the entire row is zero
            continue  # Skip the row if it is all zeros

        if matrix[i][i] == 0:  # If the pivot element is zero, swap with a lower row
            for k in range(i+1, n):
                if matrix[k][i] != 0:
                    matrix[[i, k]] = matrix[[k, i]]
                    break
            else:
                continue  # If no swap is possible, skip this iteration

        diag_element = matrix[i][i]
        matrix[i] = matrix[i] / diag_element  # Normalize the pivot row
        
        for j in range(n):
            if j != i:
                row_factor = matrix[j][i]
                matrix[j] = matrix[j] - row_factor * matrix[i]  # Eliminate other entries in the column
        
    return matrix
def row_echelon_form(matrix):
    matrix = matrix.astype(float)
    n, m = matrix.shape
    lead = 0
    
    for r in range(n):
        if lead >= m:
            return matrix
        i = r
        while matrix[i, lead] == 0:
            i += 1
            if i == n:
                i = r
                lead += 1
                if m == lead:
                    return matrix
        matrix[[i, r]] = matrix[[r, i]]
        lv = matrix[r, lead]
        matrix[r] = matrix[r] / lv
        for i in range(n):
            if i != r:
                lv = matrix[i, lead]
                matrix[i] = matrix[i] - lv * matrix[r]
        lead += 1
    return matrix
def gauss_jordan_inverse(matrix):
    rows,cols=A.shape
    if rows!=cols:
        raise IndexError("Non-square matrix, cannot get inverse") 
    n = len(matrix)
    I = np.eye(n)
    AI = np.hstack((matrix, I))
    AI = row_reduce(AI)
    A_inv = AI[:, n:]
    return A_inv

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

def solution_matrix(A,B):
    if len(A)!=len(B):
        raise IndexError('Matrix rank do not match, cannot get solution')
    limit = len(A[0])
    matrix = np.hstack((A,B))
    matrix = row_reduce(matrix)
    X = matrix[:,limit:]
    return X

def trace(matrix):
    rows,cols=A.shape
    if rows!=cols:
        raise IndexError("non-square matrix, cannot get trace") 
    output = 0
    for i in range(rows):
        output+=matrix[i][i]
    return output

D = np.array([[ 8, 6, 4,-2, 8],
              [ 5, 4, 3,-1, 4],
              [-2,-2,-1, 2,-3],
              [11, 6, 4, 1,11]])
C = np.array([[0,1,0],
              [1,0,0],
              [0,0,1]])
a=-1
F = np.array([[1,0,a],
              [1,2,-3],
              [a,1,0]])
G = np.array([1,1,2,0])
H = np.transpose(F)
print(row_echelon_form(H))

