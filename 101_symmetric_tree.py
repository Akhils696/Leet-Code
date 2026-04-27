"""
LeetCode 101. Symmetric Tree

Problem summary:
- Determine whether a binary tree is a mirror of itself.
"""


class Solution:
    def isSymmetric(self, root):
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                left.val == right.val
                and check(left.left, right.right)
                and check(left.right, right.left)
            )

        return check(root.left, root.right)
