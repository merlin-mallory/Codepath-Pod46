# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Input: head = [1,2,3,4]
        Output: [2,1,4,3]

        Input: head = []
        Output: []

        Input: head = [1]
        Output: [1]

        Constraints:

        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

        Plan:

        1. Create a dummy head, pointed the head
        2. While there is a head and head.next node,
            3. set left_node = current_node, and right_node = current_node.next:
            4. If right_node.next is not None, then left_node.next = left_node.next.next. Otherwise,
               left_node.next = None.
            5. right_node.next = left_node
            6. If left_node is head, then dummy_head = right_node
            7. head = head.next
        8. Return the LL
        9. Time: O(n)
        10. Space: O(1)
        '''

        if not head:
            return

        if head.next is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head

        previous_node = dummy_head

        while head and head.next:
            left_node = head
            right_node = head.next

            previous_node.next = right_node
            left_node.next = right_node.next
            right_node.next = left_node

            previous_node = left_node
            head = left_node.next

        return dummy_head.next

# [1, 2] > [2, 1]
# [1, 2, 3] > dummy.next [2, 3] > [1, 3] > [2, 1, 3]
# [1, 2, 3, 4] > [
