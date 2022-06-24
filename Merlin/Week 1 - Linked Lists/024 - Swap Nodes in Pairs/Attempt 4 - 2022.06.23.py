# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/swap-nodes-in-pairs/
        Input: head = [1,2,3,4]
        Output: [2,1,4,3]

        Input: head = []
        Output: []

        Input: head = [1]
        Output: [1]

        Constraints:

        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

        1. Create a dummy node and previous node.
        2. Loop through the list, swapping two nodes at a time.
        3. While there is root and root.next:
            2. left = root, right = root.next
            3. temp = right
            4. If there is right.next, then left.next = right.next, else left.next = None.
            5. temp.next = left
            6. previous.next = temp
            7. root = root.next.next
        8. return dummy.next
        9. Time complexity: O(n)
        10. Space complexity: O(1)
        '''

        if not head:
            return None

        if head.next is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = head
        previous = dummy_head

        while head and head.next:
            # Define the nodes
            left_node = head
            right_node = head.next

            # Connect the previous to the right, then the left.next to the right.next, then right.next to left.
            previous.next = right_node
            left_node.next = right_node.next
            right_node.next = left_node

            # Reinitializing the head tand previous for the next swap
            previous = left_node
            head = left_node.next

        return dummy_head.next


