from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(nums[i])
                
        while 0 in nums:
            nums.remove(0)
        nums.extend(zeros)
        return nums
    
    
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))