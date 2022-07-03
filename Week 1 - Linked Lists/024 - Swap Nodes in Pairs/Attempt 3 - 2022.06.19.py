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
        1. Create a previous node, and set the .next value to the head.
        2. While head and head.next:
            temp = head.next
            if temp.next is not None:
                head.next = head.next.next
            else:
                head.next is None
            temp.next = head
            prev.next = temp
            head = head.next
        3. Return prev.next
        4. Time: O(n)
        5. Space: O(1)
        '''

        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy

        while head and head.next:
            left_node = head
            right_node = head.next

            prev.next = right_node
            left_node.next = right_node.next
            right_node.next = left_node

            prev = left_node
            head = left_node.next

        return dummy.next
