"""
LeetCode 219. Contains Duplicate II

Problem summary:
- Return True if there are two equal values whose indices differ by at most k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for index in range(len(nums)):
            if nums[index] in window:
                return True

            window.add(nums[index])
            if len(window) > k:
                window.remove(nums[index - k])

        return False
