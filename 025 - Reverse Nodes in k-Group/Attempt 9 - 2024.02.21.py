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
        """
        # Create fetch_kth_node(node) function.
        def fetch_kth_node(node, k):
            while node and (k>0):
                node = node.next
                k -= 1
            return node

        # Setup dummy, left_seg
        dummy = ListNode(-1, head)
        left_seg = dummy

        # Infinite loop
        while True:
            # Call fetch_kth_node(left_seg), and set to mid_seg.
            mid_seg = fetch_kth_node(left_seg, k)

            # If mid_seg is None, then break out of the loop.
            if not mid_seg:
                break

            # Set right_seg = mid_seg.next
            right_seg = mid_seg.next

            # Reverse k nodes from left_seg.next
            prev = right_seg
            cur = left_seg.next
            while (cur != right_seg):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # Reattach reversed segment to left_seg and right_seg
            temp = left_seg.next
            left_seg.next = prev

            # Move left_seg pointer to temp.
            left_seg = temp

        return dummy.next
