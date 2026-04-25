"""
LeetCode 222. Count Complete Tree Nodes

Problem summary:
- Return the number of nodes in a complete binary tree.
"""


class Solution:
    def countNodes(self, root):
        def left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
