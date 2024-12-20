from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1)!=set(word2):
            return False
        
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)
        
        
        return sorted(freq_word1.values()) == sorted(freq_word2.values())


soultion = Solution()
print(soultion.closeStrings('abc', 'bca'))
