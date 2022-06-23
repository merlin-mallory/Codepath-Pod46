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
        '''

