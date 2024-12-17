class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        list_of_letters = [ch for ch in s]
        
        collected_vowels = []
        for i in range(len(list_of_letters)):
            if list_of_letters[i] in vowels:
                collected_vowels.append(list_of_letters[i])
                list_of_letters[i]=0
        reversed_list_vowels = list(reversed(collected_vowels))
        index = 0
        for i in range(len(list_of_letters)):
            if list_of_letters[i] == 0:
                list_of_letters[i] = reversed_list_vowels[index]
                index+=1
        
        string_reverse_vowels = ''.join(list_of_letters)
        return string_reverse_vowels

                
            
solution = Solution()
print(solution.reverseVowels("leetcode"))