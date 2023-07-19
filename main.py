a = int(input())
b = int(input())
matrix = []
for l in range(a):
    row = []
    for j in range(b):
        e = int(input())
        row.append(e)
    matrix.append(row)
d_s = 0
for i in range(len(matrix)):
    d_s += matrix[l][l]
print(d_s)
