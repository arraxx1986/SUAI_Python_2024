matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = 0
for i in range(len(matrix)):
    for k in range(len(matrix)-2):
        s = s + (matrix[i][k]*matrix[i][k+1]*matrix[i][k+2])*len(matrix[i])
print(s*len(matrix))
