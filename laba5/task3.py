import numpy as np

def task3(A, z):
    index = (np.abs(A-z)).argmin()
    print(A[index])


A = np.arange(10)
z = np.random.uniform(0, 10)

print(A)
print(z)

task3(A, z)
