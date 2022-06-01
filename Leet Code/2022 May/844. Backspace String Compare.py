class Solution:
    def backspaceCompare(self, s, t):
        def generateString(string):
            hash_count = 0
            for char in string:
                if char == "#": hash_count += 1
                elif hash_count: hash_count -= 1
                else: yield char
        str_1 = [i for i in generateString(s[::-1])]
        str_2 = [j for j in generateString(t[::-1])]
        return str_1 == str_2