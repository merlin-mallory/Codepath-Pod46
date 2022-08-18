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
        1. Create a reverse_ll_by_k function.
        2. Create a detect_if_next_k_is_reversible function. This will return a boolean, as well as tail_after_reverse.
        3. Create a dummy. Set previous = dummy. Check if the head is reversible. If so, then set previous.next to the
        head of the reversed LL. Set current = previous.next. Then iterate k through the current. Then set
        current.next to tail_after_reverse, and previous = current, and current = current.next. Keep looping until
        finished.
        """
        dummy = ListNode(-1)
        previous = dummy
        current = head

        while current:
            can_reverse, tail_after_reverse = self.detect_if_next_k_is_reversible(head, k)
            if can_reverse:
                previous.next = self.reverse_ll_by_k(head, k)
                current = previous.next
                for i in range(k-1):
                    current = current.next
                current.next = tail_after_reverse
                previous = current
                current = current.next

        return dummy.next


    def reverse_ll_by_k(self, node, k):
        previous = None
        current = node
        while k:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            k -= 1
        return previous

    def detect_if_next_k_is_reversible(self, node, k):
        k = k - 1
        while k and node:
            node = node.next
            k -= 1
        if not node:
            return (False, None)
        else:
            tail_after_reverse = node.next
            return (True, tail_after_reverse)
