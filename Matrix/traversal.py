matrix = [
    [1,2,3],
    [3,2,1],
    [0,0,0]
]

matrix2 = [
    [1,2,3,4],
    [3,2,1,5],
    [0,0,0,6]
]

matrix3 = [
    [1,2],
    [3,2],
    [0,0]
]

def check_rows(matrix):
    print("\nrows:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=", ")
        print()

def check_columns(matrix):
    print("\ncolumns:")
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            print(matrix[j][i], end=", ")
        print()

def check_top_left_to_bot_right_diagonals(matrix):
    print("\nmain diagonals:")
    def recurse(i, j):
        if i >= len(matrix) or j >= len(matrix[i]):
            print()
            return
        print(matrix[i][j], end=", ")
        recurse(i + 1, j + 1)
    
    for i in range(len(matrix)):
        recurse(i, 0)
    
    for i in range(1, len(matrix[0])):
        recurse(0, i)

def check_top_right_to_bot_left_diagonals(matrix):
    print("\nanti diagonals:")
    def recurse(i, j):
        if i >= len(matrix) or j < 0:
            print()
            return
        print(matrix[i][j], end=", ")
        recurse(i + 1, j - 1)
    
    for i in range(len(matrix)):
        recurse(i, len(matrix[0]) - 1)
    
    for i in range(len(matrix[0]) - 2, -1, -1):
        recurse(0, i)

# rows: 
# 1, 3, 0
# 2, 2, 0 
# 3, 1, 0
check_rows(matrix)

# columns
# 1, 3, 0
# 2, 2, 0
# 3, 1, 0
check_columns(matrix)

# main diagonals:
# 1, 2, 0
# 3, 0
# 0
# 3, 0
# 2, 0
# 1
check_top_left_to_bot_right_diagonals(matrix)

# anti diagonals:
# 3, 2, 0
# 1, 0
# 0
# 2, 3
# 1
check_top_right_to_bot_left_diagonals(matrix)