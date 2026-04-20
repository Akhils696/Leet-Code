"""
LeetCode 169. Majority Element

Problem summary:
- Return the element that appears more than n / 2 times in the array.
"""


class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
