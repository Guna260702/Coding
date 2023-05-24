import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np. array([[9,8,7],[6,5,4],[3,2,1]])
c = np.zeros([3,3],int)
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(a)):
            c[i][j] += a[i][k]*b[k][j]

print("Matrix Multiplication of a\n",a,"\nand b\n",b,"is:\n")
print(c)