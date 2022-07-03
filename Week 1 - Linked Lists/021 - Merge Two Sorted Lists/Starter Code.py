# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Input: list1 = [], list2 = []
        Output: []

        Input: list1 = [], list2 = [0]
        Output: [0]

        Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

        Plan 1:
        1. Create a new list.
        2. Use the two pointer solution to iterate through both lists, adding to the resultant list
        '''

        previous_head = ListNode(-1)

        previous = previous_head
        while list1 and list2:
            if list1.val <= list2.val:
                previous.next = list1
                list1 = list1.next
            else: # list1.val > list2.val
                previous.next = list2
                list2 = list2.next

            previous = previous.next

        if list1 is not None:
            previous.next = list1

        if list2 is not None:
            previous.next = list2

        return previous_head.next


    # Input: list1 = [1, 2, 4], list2 = [1, 3, 4], new_list = [1, 3, 4]
    # Output: [1, 1, 2, 3, 4, 4]