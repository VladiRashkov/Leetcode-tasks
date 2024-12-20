from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        set_1 = set(arr)
        occ = []
        for el in set_1:
            current = arr.count(el)
            if current not in occ:
                occ.append(current)
            else:
               return False
            
        return True
        
    
solution = Solution()
print(solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))