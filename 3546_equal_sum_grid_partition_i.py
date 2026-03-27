"""
LeetCode 3546. Equal Sum Grid Partition I

Problem summary:
- You are given an m x n grid of positive integers.
- Determine whether a single horizontal or vertical cut can split the grid
  into two non-empty parts with equal sums.
- Return True if such a cut exists, otherwise return False.
"""


class Solution:
    def canPartitionGrid(self, grid):
        rows, cols = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        running_sum = 0
        for row in range(rows - 1):
            running_sum += sum(grid[row])
            if running_sum * 2 == total_sum:
                return True

        running_sum = 0
        for col in range(cols - 1):
            for row in range(rows):
                running_sum += grid[row][col]
            if running_sum * 2 == total_sum:
                return True

        return False
