"""
LeetCode 206. Reverse Linked List

Problem summary:
- You are given the head of a singly linked list.
- Reverse the list and return the new head.
"""


class Solution:
    def reverseList(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous
