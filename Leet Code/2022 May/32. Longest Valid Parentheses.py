class Solution:
    def longestValidParentheses(self, string):
        opening, closing = '(', ')'
        stack = [-1]
        result = 0
        
        for index, parantheses in enumerate(string):
            if parantheses == opening:
                stack.append(index)
            if parantheses == closing:
                stack.pop()
                if stack:
                    result = max(result, index - stack[-1])
                else:
                    stack.append(index)
        
        return result