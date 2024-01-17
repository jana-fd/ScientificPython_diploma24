import numpy as np

class MyMatrix:
    def __init__(self, N):
        self.N = N
        self.arr = np.random.random((self.N,self.N))

    def inverse(self):
        return np.linalg.inv(self.arr)

    def determinant(self):
        return np.linalg.det(self.arr)

    def eigenvalues(self):
        return np.linalg.eigvals(self.arr)

    def __add__(self, other):
        return self.arr + other.arr

    def __mul__(self, other):
        return np.matmul(self.arr, other.arr)

if __name__ == '__main__':
    N=4
    matrix1=MyMatrix(N) #creates a square matrix
    matrix2=MyMatrix(N)
    print(matrix1.inverse())
    print(matrix1.determinant())
    print(matrix1.eigenvalues())
    print(matrix1+matrix2)
    print(matrix1*matrix2)
