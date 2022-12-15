# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/rotate-list/description/
        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]

        Input: head = [0,1,2], k = 4
        Output: [2,0,1]

        Constraints:

        The number of nodes in the list is in the range [0, 500].
        -100 <= Node.val <= 100
        0 <= k <= 2 * 109

        Plan 1:
        1. Save the oldhead and oldhead.next, loop through the LL to the final node, make final_node.next oldhead,
        and make the new head equal to the oldhead.next. We will do this k times.
        2. Time: O(n*k), Space: O(1)

        Plan 2:
        1. Mathematically calculate the new head and new tail, and just loop through the LL once, rewriting the head
        and tail connections. We will use a dummy to hold the reference to the new head.
        2. New head: k % len(LL) units to the right, make that the new_head.
        3. Then move len(LL)-1, creating a cycle when we reach the end of the loop. This node will be new_tail,
        and set the new_tail.next to None. Then set the dummy.next to the new_head.
        4. Time: O(n), Space: O(1)
        '''

        if not head:
            return None

        if head.next is None:
            return head

        old_tail = head
        old_head = head

        ll_len = 1
        while old_tail.next is not None:
            ll_len += 1
            old_tail = old_tail.next
        old_tail.next = head


        new_head_offset = ll_len - (k % ll_len)
        new_tail_offset = new_head_offset - 1

        new_tail = head
        for i in range(new_tail_offset):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None

        return new_head
