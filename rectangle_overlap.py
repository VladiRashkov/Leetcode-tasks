class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
       
        if x1 >= x4 or x3 >= x2 or y1 >= y4 or y3 >= y2:
            return False
        
       
        return True


solution = Solution()
print(solution.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])) 
print(solution.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])) 
print(solution.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]))  
