# Multiple Linear Regression
import numpy as np

def multiple_linear_regression(matrix_input, matrix_output):
    matrix_x = np.array([[1]+matrix_input[i][:-1] for i in range(len(matrix_input))])
    matrix_y = [matrix_input[i][-1] for i in range(len(matrix_input))]
    
    transpose = matrix_x.transpose()
    inverse = np.linalg.inv(np.dot(transpose,matrix_x))
    B = inverse.dot(transpose).dot(matrix_y)
    output = np.array([[1]+matrix_output[i] for i in range(len(matrix_output))])
    for i in output:
        print(B.dot(i))