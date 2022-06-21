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
        1. Convert each LL to a reversed string.
        2. Convert the reversed strings to integers.
        3. Add the integers together.
        4. Convert the resultant int to a reversed string.
        5. Construct and return the desired sum linked list.
        6. Time: O(n)
        7. Space: O(n)

        Plan 2:
        1. Calculate the length of both LL.
        2. Loop through both lists, adding the shorter LL's value to the longer LL's value.
           If the sum is >= 10, deduct 10 from the value, and carry the one to next value.
        3. Eventually we'll reach the end of the shorter list. Continuing carrying values
           through the longer list. If there is a carry at the final node, create a new node
           with a value of 1 at the end.
        4. Return the resultant list.
        5. Time: O(n)
        6. Space: O(1)
        '''

        def calcuate_len(node):
            len_counter = 0
            while node:
                len_counter += 1
                node = node.next
            return len_counter

        l1_len = calcuate_len(l1)
        l2_len = calcuate_len(l2)

        if l1_len >= l2_len:
            longer_len_list = l1
            shorter_len_list = l2
        else:
            longer_len_list = l2
            shorter_len_list = l1

        dummy_head = ListNode(-1)
        dummy_head.next = longer_len_list

        while shorter_len_list:
            longer_len_list.val += shorter_len_list.val

            if longer_len_list.val >= 10:
                longer_len_list.val -= 10
                if longer_len_list.next is not None:
                    longer_len_list.next.val += 1
                else:
                    longer_len_list.next = ListNode(1)

            longer_len_list = longer_len_list.next
            shorter_len_list = shorter_len_list.next

        while longer_len_list:
            if longer_len_list.val >= 10:
                longer_len_list.val -= 10
                if longer_len_list.next is not None:
                    longer_len_list.next.val += 1
                else:
                    longer_len_list.next = ListNode(1)
            longer_len_list = longer_len_list.next

        return dummy_head.next
