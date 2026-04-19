"""
LeetCode 118. Pascal's Triangle

Problem summary:
- Return the first numRows of Pascal's triangle.
"""


class Solution:
    def generate(self, numRows):
        triangle = []

        for row_index in range(numRows):
            row = [1] * (row_index + 1)
            for col_index in range(1, row_index):
                row[col_index] = (
                    triangle[row_index - 1][col_index - 1]
                    + triangle[row_index - 1][col_index]
                )
            triangle.append(row)

        return triangle
