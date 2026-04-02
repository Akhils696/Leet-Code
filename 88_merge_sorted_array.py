"""
LeetCode 88. Merge Sorted Array

Problem summary:
- You are given two sorted integer arrays, nums1 and nums2.
- Merge nums2 into nums1 as one sorted array in non-decreasing order.
- Modify nums1 in-place and do not return anything.
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        write = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
