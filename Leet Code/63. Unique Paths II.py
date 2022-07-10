class Solution:
    def uniquePathsWithObstacles(self, matrix):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                matrix[i][j] = 0 if matrix[i][j] else 1
                    
                if matrix[i][j]:
                    if (i - 1) >= 0 and (j - 1) >= 0:
                        matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
                    elif (i - 1) >= 0:
                        matrix[i][j] = matrix[i - 1][j]
                    elif (j - 1) >= 0:
                        matrix[i][j] = matrix[i][j - 1]
        
        return matrix[ROWS - 1][COLS - 1]