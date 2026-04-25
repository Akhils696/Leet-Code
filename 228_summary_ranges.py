"""
LeetCode 228. Summary Ranges

Problem summary:
- Return the smallest sorted list of ranges that covers all numbers in a
  sorted unique integer array.
"""


class Solution:
    def summaryRanges(self, nums):
        result = []
        index = 0

        while index < len(nums):
            start = nums[index]

            while index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                index += 1

            if start == nums[index]:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(nums[index]))

            index += 1

        return result
