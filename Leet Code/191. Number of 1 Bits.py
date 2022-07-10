class Solution:
    def hammingWeight(self, binary):
        count = 0
        while binary:
            binary &= binary - 1
            count += 1
        return count