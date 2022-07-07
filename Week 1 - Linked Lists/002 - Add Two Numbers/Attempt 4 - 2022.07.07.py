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

        N is in range 1-100
        Node.val are only digits 0-9
        There are no leading zeros

        Plan:
        1. Calculate the length of the two LL
        2. Loop through the shorter LL and longer LL, and add all of the shorter LL's vals to the longer LL's vals.
        If the longer LL's .next val exists, then carry ones to the .next node. Otherwise, create a new 1 value node
        in the longer LL.
        3. Loop through the remainder of the longer LL, and continue the carrying process.
        4. Return the final LL
        5. Time: O(m+n), where m = len(l1) and n = len(l2). Space: O(1)
        '''
        def calculate_len(node):
            node_len = 0
            while node is not None:
                node_len += 1
                node = node.next
            return node_len

        l1_len = calculate_len(l1)
        l2_len = calculate_len(l2)

        if l1_len >= l2_len:
            longer_LL = l1
            shorter_LL = l2
        else:
            longer_LL = l2
            shorter_LL = l1

        dummy = ListNode(1)
        dummy.next = longer_LL

        while shorter_LL:
            longer_LL.val = longer_LL.val + shorter_LL.val
            if longer_LL.val >= 10:
                longer_LL.val -= 10
                if longer_LL.next is not None:
                    longer_LL.next.val += 1
                else:
                    longer_LL.next = ListNode(1)
            shorter_LL = shorter_LL.next
            longer_LL = longer_LL.next

        while longer_LL:
            if longer_LL.val >= 10:
                longer_LL.val -= 10
                if longer_LL.next is not None:
                    longer_LL.next.val += 1
                else:
                    longer_LL.next = ListNode(1)
            longer_LL = longer_LL.next

        return dummy.next

