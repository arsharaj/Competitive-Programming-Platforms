class Solution:
    def findUnsortedSubarray(self, nums):        
        sorted_nums = sorted(nums)
        start = end = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start == -1:
                    start, end = i, i + 1
                else:
                    end = i + 1
        return end - start