# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]

        N is in range 1-100
        Node.val are only digits 0-9
        There are no leading zeros

        Plan 1:

        1. Create strings to represent both lists.
        2. Loop through each linked list and concatenate the results
        3. Convert both strings to integers
        4. Calculate the sum
        5. Create a new linked list

        Plan 2:
        1. Calculate the length of both linked lists
        2. Add the smaller list's values to the bigger list's values, carrying ones as necessary
        3. If the final digit of the larger list carries, then we need to add an extra node.
        '''

