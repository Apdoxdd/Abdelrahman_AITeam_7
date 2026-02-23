def matsum (arr1,arr2):
    rows_1 = len(arr1)
    rows_2 = len(arr2)
    cols_1 = len(arr1[0]) if rows_1>0 else 0
    cols_2 = len(arr2[0]) if rows_2>0 else 0
    if rows_1 != rows_2 or cols_1 != cols_2:
        print("Invalid matrix dimentions. ")
        return None
    result = [[0 for _ in range (cols_1)] for _ in range (rows_1)]
    for i in range (0,rows_1):
        for j in range(0,cols_1):
            result[i][j]= arr1[i][j]+arr2[i][j]

    return result
def matsub (arr1,arr2):
    rows_1 = len(arr1)
    rows_2 = len(arr2)
    cols_1 = len(arr1[0]) if rows_1>0 else 0
    cols_2 = len(arr2[0]) if rows_2>0 else 0
    if rows_1 != rows_2 or cols_1 != cols_2:
        print("Invalid Matrices dimensions") 
        return None
    result = [[0 for _ in range (cols_1)] for _ in range (rows_1)]
    for i in range(rows_1):
        for j in range (cols_1):
            result[i][j] = arr1[i][j] - arr2[i][j]
    return result

def scalarsum (scalar,arr):
    rows  = len(arr)
    cols = len(arr[0]) if rows>0 else 0
    result = [[0 for _ in range (cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j]=arr[i][j]+scalar
    return result

def scalarsub (scalar,arr):
    rows  = len(arr)
    cols = len(arr[0]) if rows>0 else 0
    result = [[0 for _ in range (cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j]=arr[i][j]-scalar
    return result

def scalarmul (scalar,arr):
    rows  = len(arr)
    cols = len(arr[0]) if rows>0 else 0
    result = [[0 for _ in range (cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j]=arr[i][j]*scalar
    return result
               
def matmul (arr1,arr2):
    rows1 = len(arr1)
    cols1 = len(arr1[0]) if rows1>0 else 0
    rows2 = len(arr2)
    cols2 = len(arr2[0]) if rows2>0 else 0
    if cols1 != rows2:
        print("Invalid dimenstions, cols 1 should be equal to rows 2")
        return None
    result = [[0 for _ in range(cols2)]for _ in range (rows1)]
    for m in range (rows1):
        
        for i in range(cols2):
            element = 0
            for j in range(cols1):
                element += arr1[m][j]*arr2[j][i]
            result[m][i] = element
    return result            


def matnorm(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows>0 else 0
    max = [float('-inf')] * cols # 34an n3ml store l max value in row
    min = [float('inf')]*cols # same but min
    for i in range(cols):
        for j in range(rows):
            if arr[j][i] > max[i]: max[i] = arr[j][i]
            if arr[j][i] < min[i]: min[i] = arr[j][i]
    result = [[0  for _ in range(cols)] for _ in range(rows)]
    for i in range(cols):
        for j in range(rows):
            result[j][i] = (arr[j][i]-min[i])/(max[i]-min[i]) if max[i] - min[i] != 0 else 0
    return result        