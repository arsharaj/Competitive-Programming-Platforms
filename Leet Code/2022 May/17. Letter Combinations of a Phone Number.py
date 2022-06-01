class Solution:
    def letterCombinations(self, digits):
        dictionary = { 
            '2' : ['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']
        }
        
        if len(digits) == 0:
            return []
        
        result = None
        for num in digits:
            if result == None:
                result = dictionary[num]
            else:
                combinations = []
                for i in result:
                    for j in dictionary[num]:
                        combinations.append(i + j)
                result = combinations
                
        return result