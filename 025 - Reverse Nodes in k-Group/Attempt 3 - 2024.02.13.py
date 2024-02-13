# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/reverse-nodes-in-k-group/

        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is
        not a multiple of k then left-out nodes, in the end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes themselves may be changed.

        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]

        Input: head = [1,2,3,4,5], k = 3
        Output: [3,2,1,4,5]

        Constraints:
        The number of nodes in the list is n.
        1 <= k <= n <= 5000
        0 <= Node.val <= 1000

        Linked List
        Create dummy to head
        l2 = dummy
        Loop while l2
            left_seg = l2
            for i in range(k):
                l2 = l2.next
            right_seg = l2
            l2.next = None

            Reverse left_seg.

            for i in range(k):
                left_seg = left_seg.next
            left_seg.next = right_seg
            left_seg = left_seg.next
        Time: O(n)
        Space: O(1)
        Edge: None, but could be only one node
        """
        # Failed Attempt
        dummy = ListNode(0, head)
        l2 = dummy
        while l2:
            # Chop to left and right segments
            left_seg = l2
            for i in range(k):
                l2 = l2.next
            right_seg = l2
            l2.next = None

            # Reverse left seg
            prev = None
            cur = left_seg
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            left_seg = prev

            # Advance left_seg
            for i in range(k):
                left_seg = left_seg.next
            left_seg.next = right_seg
            l2 = left_seg
            l2 = l2.next
        return dummy.next
