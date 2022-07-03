# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''

        Input: l1 = [7,2,4,3], l2 = [5,6,4]
        Output: [7,8,0,7]

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [8,0,7]

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Constraints:

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.
        '''