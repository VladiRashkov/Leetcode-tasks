class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum+=nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
        return max_sum/k

solution = Solution()
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))  
