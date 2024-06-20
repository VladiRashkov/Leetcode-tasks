class Solution(object):
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return []



nums = [2,11,7,15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))