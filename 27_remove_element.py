"""
LeetCode 27. Remove Element

Problem summary:
- Remove all occurrences of val from nums in-place.
- Return the number of elements not equal to val.
"""


class Solution:
    def removeElement(self, nums, val):
        count = 0

        for number in nums:
            if number != val:
                nums[count] = number
                count += 1

        return count
