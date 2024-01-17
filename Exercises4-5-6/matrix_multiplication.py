%%timeit
import numpy as np
def matrix_multiplication(m1,m2):
    size1 = m1.shape
    size2 = m2.shape

    m3 = np.zeros((size1[0],size2[1]))
    if(size1[1] != size2[0]):
        print('Cannot multiply the matrices')
        return
    for i in range(size1[0]):
        for j in range(size2[1]):
            for k in range(size2[0]):
                m3[i,j] += m1[i,k]*m2[k,j]
    return m3
A = np.array([[1,77,3],[4,5,6],[7,8,9]])
B = np.array([[2,23,49],[3,49,50],[23,4,56]])
matrix_multiplication(A,B)
#print(matrix_multiplication(A,B))
