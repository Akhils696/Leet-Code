"""
LeetCode 119. Pascal's Triangle II

Problem summary:
- Return the rowIndex-th row of Pascal's triangle.
"""


class Solution:
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)

        for current_row in range(2, rowIndex + 1):
            for index in range(current_row - 1, 0, -1):
                row[index] += row[index - 1]

        return row
