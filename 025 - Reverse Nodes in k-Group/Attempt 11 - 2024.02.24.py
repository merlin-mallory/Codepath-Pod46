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
        Create fetch_kth_node(node) function. Returns node.
        Set up dummy.
        Set left_seg = head.
        Loop infinitely
            Call fetch_kth_node(left_seg). Set to mid_seg.
            If mid_seg is None, then break out of the infinite loop.
            Set right_seg = mid_seg.next
            Reverse k nodes from mid_seg
            Reattach pointers between left_seg, mid_seg, and right_seg
            Advance left_seg pointer to right_seg.
        Return dummy.next.
        Time: O(n)
        Space: O(1)
        Edge: Could be just 1 node in head.
        """
        def fetch_kth_node(node, k):
            while node and (k > 0):
                node = node.next
                k -= 1
            return node

        dummy = ListNode(-1, head)
        left_seg = dummy
        while True:
            mid_seg = fetch_kth_node(left_seg, k)
            if not mid_seg:
                break
            right_seg = mid_seg.next

            prev = right_seg
            cur = left_seg.next
            while (cur != right_seg):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = left_seg.next
            left_seg.next = prev
            left_seg = temp

        return dummy.next

