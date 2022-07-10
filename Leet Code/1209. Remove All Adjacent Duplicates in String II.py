class Solution:
    def removeDuplicates(self, string, limit):
        stack = []  # [char, count]
        for char in string:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
                
            if stack[-1][1] == limit:
                stack.pop()
        
        result = ""
        for char, count in stack:
            result += (char * count)
        
        return result