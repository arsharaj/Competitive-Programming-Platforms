class Solution:
    def combinationSum3(self, depth, required_sum):
        result = []
        
        # Backtrack
        def backtrack(val, new_depth, combination):
            if new_depth == 0:
                if sum(combination) == required_sum:
                    result.append(combination)
                return
            
            for i in range(val + 1, 10):
                backtrack(i, new_depth - 1, combination + [i])
        
        # Backtrack all valid possible combinations and add them to result
        # when the contraints are fulfilled
        for i in range(1, 10):
            backtrack(i, depth - 1, [i])
        
        return result