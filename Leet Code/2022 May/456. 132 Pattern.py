class Solution:
    def find132pattern(self, nums) -> bool:
        stk = []
        top = -float("inf")

        for i in range(len(nums) -1, -1, -1):
            if top > nums[i]:
                return True

            while(len(stk) and nums[i] > stk[len(stk) -1]):
                top = stk.pop()
            stk.append(nums[i])
        return False