class Solution:
    def missingNumber(self, nums):
        size = len(nums)
        expected = size * (size + 1) // 2
        actual = sum(nums)
        return expected - actual