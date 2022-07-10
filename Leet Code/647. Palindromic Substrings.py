class Solution:
    def countSubstrings(self, string: str) -> int:
        size = len(string)
        count = 0
        for i in range(size):
            check_string = ""
            for j in range(i, size):
                check_string += string[j]
                if check_string == check_string[::-1]:
                    count += 1
        return count