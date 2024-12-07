# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


x = int(input())
y = int(input())
z = int(input())
n = int(input())

listof = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != n:
                listof.append([i, j, k])
print(listof)
