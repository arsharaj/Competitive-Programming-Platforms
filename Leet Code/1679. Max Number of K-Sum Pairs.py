class Solution:
    def maxOperations(self, nums, k):
        operations = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            summation = nums[left] + nums[right]
            if summation == k:
                operations += 1
                left += 1
                right -= 1
            elif summation > k:
                right -= 1
            else:
                left += 1
        return operations