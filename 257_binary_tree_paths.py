"""
LeetCode 257. Binary Tree Paths

Problem summary:
- You are given the root of a binary tree.
- Return all root-to-leaf paths in any order.
"""


class Solution:
    def binaryTreePaths(self, root):
        result = []

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return result
