# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
import math

def gcd_of_strings(word1, word2):
   
    if word1 + word2 != word2 + word1:
        return ''

   
    gcd_length = math.gcd(len(word1), len(word2))
    return word1[:gcd_length]


word1 = "ABCABC"
word2 = "ABC"
print(gcd_of_strings(word1, word2))  
word1 = "ABABAB"
word2 = "ABAB"
print(gcd_of_strings(word1, word2)) 

word1 = "LEET"
word2 = "CODE"
print(gcd_of_strings(word1, word2)) 
