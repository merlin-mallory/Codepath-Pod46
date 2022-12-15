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
        '''
        l1_len = self.calculate_length(l1)
        l2_len = self.calculate_length(l2)

        if l1_len <= l2_len:
            shorter_LL = l1
            longer_LL = l2
        else:
            shorter_LL = l2
            longer_LL = l1

        dummy = longer_LL

        while shorter_LL:
            longer_LL.val = shorter_LL.val + longer_LL.val
            if longer_LL.val >= 10:
                longer_LL.val -= 10
                if longer_LL.next:
                    longer_LL.next.val += 1
                else:
                    longer_LL.next = ListNode(1)
            longer_LL = longer_LL.next
            shorter_LL = shorter_LL.next

        while longer_LL:
            if longer_LL.val >= 10:
                longer_LL.val -= 10
                if longer_LL.next:
                    longer_LL.next.val += 1
                else:
                    longer_LL.next = ListNode(1)
            longer_LL = longer_LL.next

        return dummy

    def calculate_length(self, ll):
        counter = 0
        while ll:
            counter += 1
            ll = ll.next
        return counter

