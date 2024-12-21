import string

class Solution:
    def decodeString(self, s: str) -> str:
        numbers = [] 
        chars = []  
        current_string = ''  
        current_number = 0  
        
        for i in s:
            if i.isnumeric():
                current_number = current_number * 10 + int(i)
            elif i == '[':
                numbers.append(current_number)
                chars.append(current_string)
                current_string = ''
                current_number = 0
            elif i == ']':
                multiplier = numbers.pop()
                previous_string = chars.pop()
                current_string = previous_string + current_string * multiplier
            elif i in string.ascii_letters:
                current_string += i
        
        return current_string

# Example usage:
solution = Solution()
print(solution.decodeString("3[a2[c]]"))  # Output: accaccacc
