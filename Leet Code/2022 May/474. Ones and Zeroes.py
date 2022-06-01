class Solution:
    def findMaxForm(self, strs, zeros, ones):
        dp = [[0 for _ in range(ones + 1)] for _ in range(zeros + 1)]
        
        for string in strs:
            zeros_count = string.count('0')
            ones_count = string.count('1')
            for i in range(zeros, zeros_count - 1, -1):
                for j in range(ones, ones_count - 1, -1):
                     dp[i][j] = max(dp[i - zeros_count][j - ones_count] + 1, dp[i][j])
                        
        return dp[zeros][ones]