import numpy as np

# Khai báo ma trận và vector
M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:")
print(M1)

u = np.array([2, 1])
print("Vector u:")
print(u)

# Tích M1 * u
print("Tích M1 . u:")
tichM1u = M1.dot(u)
print(tichM1u)

# Tích u * M1
print("Tích u . M1:")
tichuM1 = u.dot(M1)
print(tichuM1)

# Dùng np.dot
print("np.dot(M1, u):")
print(np.dot(M1, u))

print("np.dot(u, M1):")
print(np.dot(u, M1))

# Ma trận zeros và ones
mat1 = np.zeros([5, 5])
print("mat1 (zeros):")
print(mat1)

mat2 = np.ones([5, 5])
print("mat2 (ones):")
print(mat2)

mat3 = mat1 + 2 * mat2
print("mat3 = mat1 + 2*mat2:")
print(mat3)

# Tham chiếu giữa mat3 và mat4
mat4 = mat3
mat3[3][2] = 10
print("mat3 sau khi thay đổi phần tử [3][2] = 10:")
print(mat3)
print("mat4 cũng thay đổi theo:")
print(mat4)

# Dùng np.copy
mat5 = np.copy(mat3)
mat3[3][2] = 99
print("mat3 sau khi thay đổi phần tử [3][2] = 99:")
print(mat3)
print("mat4 (vẫn thay đổi):")
print(mat4)
print("mat5 (không thay đổi):")
print(mat5)

# Ma trận empty
mat6 = np.empty([4, 5])
print("mat6 (empty):")
print(mat6)

# Ma trận đơn vị
mat7 = np.identity(4)
print("mat7 (identity):")
print(mat7)

# Ma trận random
mat8 = np.random.random([4, 5])
print("mat8 (random):")
print(mat8)
