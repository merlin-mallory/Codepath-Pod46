# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Input: head = [1,2,3,4,5], k = 2
        Output: [4,5,1,2,3]

        Input: head = [0,1,2], k = 4
        Output: [2,0,1]

        Constraints:

        The number of nodes in the list is in the range [0, 500].
        -100 <= Node.val <= 100
        0 <= k <= 2 * 109

        Plan 1:
        1. Create counter = 0.
        2. Until counter = k, keep track of the previous node, move the node at the end of
            the list to the front of the list, and counter++
        3. Return the list
        4. Time: O((k*n))
        5. Space: O(1)

        Plan 2:
        1. Calculate the length of the list.
        2. Length of the list mod k to find the number of necessary rotations
        3. Counter = 0
        4. Until counter = necessary_rotations, rotate.
        5. Time: (O(k))
        '''

        if not head:
            return

        if head.next is None:
            return head

        def calculate_len(node):
            len_counter = 0
            while node:
                node = node.next
                len_counter += 1
            return len_counter

        head_len = calculate_len(head)
        necessary_rotations = k % head_len

        dummy_head = ListNode(-1)
        dummy_head.next = head

        rotation_counter = 0

        while rotation_counter < necessary_rotations:
            prev = None
            front_of_list = head

            while head.next is not None:
                prev = head
                head = head.next

            head.next = front_of_list
            prev.next = None

            dummy_head.next = head
            rotation_counter += 1

        return dummy_head.next


