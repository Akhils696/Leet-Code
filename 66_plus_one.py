"""
LeetCode 66. Plus One

Problem summary:
- You are given a large integer represented as an array of digits.
- Increment the integer by one.
- Return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits):
        for index in range(len(digits) - 1, -1, -1):
            if digits[index] < 9:
                digits[index] += 1
                return digits
            digits[index] = 0

        return [1] + digits
