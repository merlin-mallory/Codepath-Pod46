# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/add-two-numbers/

        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
        linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]

        Constraints:
        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

        Plan:
        1. Loop through the two LL and mark the longer_LL and shorter_LL.
        2. dummy = longer_LL.next
        3. While shorter_LL is not None, add shorter_LL's value to longer_LL's value. If the result is >= 10,
        and longer_LL.next is not None, then add +1 to longer_LL.next's value. Otherwise, set longer_LL.next to new
        Node (1). Then iterate longer_LL and shorter_LL by 1.
        4. After the shorter_LL completes, continue carrying through the remainder of the longer_LL.
        5. return dummy.next
        '''

        def calculate_len(node):
            counter = 1
            while node.next is not None:
                node = node.next
                counter += 1
            return counter

        l1_len = calculate_len(l1)
        l2_len = calculate_len(l2)

        if l1_len >= l2_len:
            longer_ll = l1
            shorter_ll = l2
        else:
            longer_ll = l2
            shorter_ll = l1

        dummy = longer_ll

        while shorter_ll is not None:
            longer_ll.val += shorter_ll.val
            if longer_ll.val >= 10:
                longer_ll.val -= 10
                if longer_ll.next is not None:
                    longer_ll.next.val += 1
                else:
                    longer_ll.next = ListNode(1)
            shorter_ll = shorter_ll.next
            longer_ll = longer_ll.next

        while longer_ll is not None:
            if longer_ll.val >= 10:
                longer_ll.val -= 10
                if longer_ll.next is not None:
                    longer_ll.next.val += 1
                else:
                    longer_ll.next = ListNode(1)
            longer_ll = longer_ll.next

        return dummy

