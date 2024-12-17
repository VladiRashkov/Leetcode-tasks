class Solution:   
    def kidsWithCandies(self, candies, extraCandies):
        list_values = []
        for i in range(len(candies)):
            temp_candies = candies.copy()
            temp_num = candies[i]+extraCandies
            temp_candies.insert(i, temp_num)
            
            max_num = max(temp_candies)
            list_values.insert(i, max_num==temp_num)
        
            temp_candies.clear()
            temp_num = 0
        return list_values


solution = Solution()
print(solution.kidsWithCandies([2,3,5,1,3], 3))
