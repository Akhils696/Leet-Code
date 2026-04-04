"""
LeetCode 94. Binary Tree Inorder Traversal

Problem summary:
- You are given the root of a binary tree.
- Return the inorder traversal of its nodes' values.
"""


class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
