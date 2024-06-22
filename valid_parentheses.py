class Solution(object):
    def isValid(self, s):
        
        for par in s:
            if par == '(':
                if ')' in s:
                    continue
                else:
                    return False
            
            if par == '[':
                if ']' in s:
                    continue
                else:
                    return False
            if par == '{':
                if '}' in s:
                    continue
                else:
                    return False
                
        return True
            
solution = Solution()

print(solution.isValid(input()))