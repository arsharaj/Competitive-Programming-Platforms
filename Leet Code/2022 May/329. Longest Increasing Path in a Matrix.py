class Solution:
    def longestIncreasingPath(self, MATRIX):
        ROWS = len(MATRIX)
        COLS = len(MATRIX[0])
        cache = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        result = 0
        
        def dfs(row, col, pre):
            if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or
                pre >= MATRIX[row][col]):
                return 0
            
            if cache[row][col] != 0:
                return cache[row][col]
            
            res = 1
            res = max(res, 1 + dfs(row + 1, col, MATRIX[row][col]))
            res = max(res, 1 + dfs(row - 1, col, MATRIX[row][col]))
            res = max(res, 1 + dfs(row, col + 1, MATRIX[row][col]))
            res = max(res, 1 + dfs(row, col - 1, MATRIX[row][col]))

            cache[row][col] = res
            
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                result = max(result, dfs(i, j, -1))
                
        return result