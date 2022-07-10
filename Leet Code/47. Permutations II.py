import itertools

class Solution:
    def permuteUnique(self, nums):
        results = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return
        
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    
                    backtrack(comb, counter)
                    
                    comb.pop()
                    counter[num] += 1
            
        backtrack([], itertools.Counter(nums))
        
        return results