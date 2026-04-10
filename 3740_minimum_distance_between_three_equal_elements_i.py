"""
LeetCode 3740. Minimum Distance Between Three Equal Elements I

Problem summary:
- Find three distinct indices i, j, and k such that nums[i] == nums[j] == nums[k].
- Return the minimum possible distance |i - j| + |j - k| + |k - i|.
- Return -1 if no such triple exists.
"""


class Solution:
    def minimumDistance(self, nums):
        positions = {}
        best = float("inf")

        for index, value in enumerate(nums):
            if value not in positions:
                positions[value] = []

            positions[value].append(index)
            if len(positions[value]) >= 3:
                best = min(best, 2 * (index - positions[value][-3]))

        return best if best != float("inf") else -1
