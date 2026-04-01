"""
LeetCode 2839. Check if Strings Can Be Made Equal With Operations I

Problem summary:
- You are given two strings of length 4.
- You may swap characters whose indices differ by 2 any number of times.
- Return True if the two strings can be made equal, otherwise return False.
"""


class Solution:
    def canBeEqual(self, s1, s2):
        return sorted((s1[0], s1[2])) == sorted((s2[0], s2[2])) and sorted(
            (s1[1], s1[3])
        ) == sorted((s2[1], s2[3]))
