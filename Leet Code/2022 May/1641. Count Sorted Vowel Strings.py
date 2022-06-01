class Solution:
    def countVowelStrings(self, n):
        def count(n, last = ""):
            if n == 0:
                return 1
            else:
                val = 0
                for vowel in ['a','e','i','o','u']:
                    if last <= vowel:
                        val += count(n - 1, vowel)
                return val
        return count(n)