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

        Plan:
        Create grab_kth_node(l1, k) function.
            Loop while k.
                Advance l1 by 1
                Decrement k by 1.
            return l1
        Create dummy linked to head
        l1 = dummy
        Loop while l1.
            left_seg = l1
            mid_seg = grab_kth_node(l1)
            right_seg = kth.next

            Reverse mid_seg (bit funky)
            mid_seg(head).prev = left_seg
            mid_seg(tail).next = right_seg
            l1 = mid_seg.next
        Return dummy.next

        Time: O(n)
        Space: O(1)
        Edge: None
        """
        def grab_kth_node(l1, k):
            while l1 and k > 0:
                l1 = l1.next
                k -= 1
            return l1

        dummy = ListNode(-1, head)
        left_seg = dummy

        while True:
            mid_seg = grab_kth_node(left_seg, k)
            if not mid_seg:
                break
            right_seg = mid_seg.next

            # Reverse mid_seg
            prev = mid_seg.next
            cur = left_seg.next
            while cur != right_seg:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = left_seg.next
            left_seg.next = mid_seg
            left_seg = temp
        return dummy.next



