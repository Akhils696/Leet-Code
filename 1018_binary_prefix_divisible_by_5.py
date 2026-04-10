"""
LeetCode 1018. Binary Prefix Divisible By 5

Problem summary:
- You are given a binary array nums.
- For each prefix of nums, determine whether its binary value is divisible by 5.
- Return the list of boolean answers.
"""


class Solution:
    def prefixesDivBy5(self, nums):
        result = []
        remainder = 0

        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            result.append(remainder == 0)

        return result
