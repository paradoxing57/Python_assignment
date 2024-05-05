def matrix_multiplication(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result_matrix = matrix_multiplication(matrix1, matrix2)
if result_matrix:
    print("Result of matrix multiplication:")
    for row in result_matrix:
        print(row)
