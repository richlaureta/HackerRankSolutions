matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

size = len(matrix)
total = 0

for i in range(size//2):
    for j in range(size//2):
        total += max(matrix[i][j], matrix[i][size-j-1],matrix[size - i - 1][j],matrix[size - i - 1][size - j -1])

print(total)