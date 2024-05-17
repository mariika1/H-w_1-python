#№10Евклидово расстояние.
import numpy as np

def task10(matrix_: np.ndarray) -> np.ndarray:

    M = [[0] * len(matrix_) for i in range(len(matrix_))] #запишем нулевую  матрицу 
# перемножим вектор i на вектор j:
    for i in range(len(matrix_)): 
        for j in range(len(matrix_)): 
            M[i][j] = np.linalg.norm(matrix_[i]-matrix_[j]) #вычислим евклидово расстояние используя функцию np.linalg.norm библиотеки numpy
                                                            #запишем полученные значения в матрицу М
    return M

print(task10(np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [-2, 5, 4]])))