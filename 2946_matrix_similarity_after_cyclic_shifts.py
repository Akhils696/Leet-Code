"""
LeetCode 2946. Matrix Similarity After Cyclic Shifts

Problem summary:
- You are given an m x n integer matrix and an integer k.
- Even-indexed rows are shifted left by k positions, and odd-indexed rows are
  shifted right by k positions.
- Return True if the matrix remains identical to the original after these
  shifts, otherwise return False.
"""


class Solution:
    def areSimilar(self, mat, k):
        rows, cols = len(mat), len(mat[0])
        k %= cols

        for row in range(rows):
            for col in range(cols):
                if row % 2 == 0:
                    if mat[row][col] != mat[row][(col + k) % cols]:
                        return False
                else:
                    if mat[row][col] != mat[row][(col - k + cols) % cols]:
                        return False

        return True
