# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

        Input: head = [1,2], pos = 0
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

        Input: head = [1], pos = -1
        Output: false
        Explanation: There is no cycle in the linked list.

        The number of the nodes in the list is in the range [0, 104].
        -105 <= Node.val <= 105
        pos is -1 or a valid index in the linked-list.
        '''

