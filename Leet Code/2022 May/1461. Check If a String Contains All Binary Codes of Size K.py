class Solution:
    def hasAllCodes(self, binary, length):
        count = set()
        size = len(binary)
        for i in range(size):
            if i + length <= size:
                count.add(binary[i : i + length])
            if len(count) == 1 << length:
                return True
        return False