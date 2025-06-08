class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []

        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(0, 10):
                next_num = curr*10+i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)
        return result

n = 13
solution = Solution()
print(solution.lexicalOrder(n))
