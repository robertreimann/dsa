grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]

class Rotate:
    def transpose(self, grid):
        for j in range(len(grid[0])):
            for i in range(j, len(grid)):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    
    def reflect(self, grid):
        for i in range(len(grid)):
            grid[i] = grid[i][::-1]

    def rotate(self, grid):
        self.transpose(grid)
        self.reflect(grid)

rotator = Rotate()

# [1,  2,  3,  4,  5]
# [6,  7,  8,  9,  10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]
for row in grid: print(row)

rotator.rotate(grid)

# [21, 16, 11, 6, 1]
# [22, 17, 12, 7, 2]
# [23, 18, 13, 8, 3]
# [24, 19, 14, 9, 4]
# [25, 20, 15, 10, 5]
for row in grid: print(row)