# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Input: head = [4,5,1,9], node = 5
        Output: [4,1,9]

        Input: head = [4,5,1,9], node = 1
        Output: [4,5,9]

        n ranges from 2 to 1000
        Each value in the node is unique
        node is guarenteed to be in list, and not be a tail node
        """
        node.val = node.next.val
        node.next = node.next.next

