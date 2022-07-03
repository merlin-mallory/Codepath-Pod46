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

        Input: head = [1, 2, 3]
        Output: [2, 1, 3]

        Constraints:

        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

        Plan:

        1. Create a dummy head to keep track of the head.
        2. Iterate through the linked list, swapping current with next, and then moving right 2.
        3. If there's an even number of nodes, then the loop will stop when current = None.
           Otherwise, if there's an odd number of nodes, then the loop will stop when
           current.next is None, after the swap.
        4. We will need to handle the edge cases with 0 and 1 nodes.
        '''

        if not head:
            return

        if head.next is None:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head

        previous_node = dummy_node

        while head and head.next:
            first_node = head
            second_node = head.next

            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            previous_node = first_node
            head = first_node.next

        return dummy_node.next
