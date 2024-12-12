# 64. Minimum Path Sum
# Medium
# Topics
# Companies
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

def minPathSum(matrix):
    collect_required = []
    start = 0
    for row in matrix:
        for col in range(start, len(row)-1):
            if col == 0:
                current = sum(row)
                collect_required.append(current)
                start=1
                break
            else:
                collect_required.append(row[len(row)-1])
                start=1
                break
        
    sum_all = sum(collect_required)
    return sum_all

grid = [[1,2,3],[4,5,6]]
print(minPathSum(grid))


