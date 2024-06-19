class Solution(object):
    def can_shift_to_goal(self, s: str, goal: str):
        if len(s) != len(goal):
            return False
        return goal in (s + s)

solution = Solution()
s1 = "abcde"
goal1 = "cdeab"

print(solution.can_shift_to_goal(s1, goal1)) 

s2 = "abcde"
goal2 = "abced"
print(solution.can_shift_to_goal(s2, goal2))  
        