class Solution:
    def canPlaceFlowers(self, bed, plant):
        count = 0
        collected_free_spots = 0
        beginning = True
        
        if len(bed) == 1 and bed[0] == 0:
            return True
        
        for i in range(len(bed)-1):
            if beginning and bed[i]==0:
                count += 1
                if count == 2:
                    collected_free_spots+=1
                    count = 1
                    beginning=False
                    continue
                else:
                    continue
            else:
                beginning = False
            if bed[i] == 0:
                count += 1
                if count == 3:
                    collected_free_spots+=1
                    count = 1
            else:
                count = 0
        
        if bed[len(bed)-1] == 0:
            count+=1
            if count>=2:
                collected_free_spots+=1
            
        
        return collected_free_spots>=plant

solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0], 1))
