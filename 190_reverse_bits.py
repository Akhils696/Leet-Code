"""
LeetCode 190. Reverse Bits

Problem summary:
- Reverse the bits of a 32-bit unsigned integer.
"""


class Solution:
    def reverseBits(self, n):
        result = 0

        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
