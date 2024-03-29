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
        1. Calculate the length of both LL. Mark the longer and shorter LLs. Set dummy to the head of the longer LL.
        2. Iterate through both LL, adding' the shorter's value to the larger's value. If the result is >= 10,
        then subtract 10, and if there is longerLL.next, then longerLL.next.val++, otherwise make a new (1) node.
        Eventually the shorter LL will be extinguished, and then we continue carrying values through the longer LL.
        3. Time: O(n), Space: O(1)
        '''
        def calculate_len(node):
            length = 1
            while node.next:
                node = node.next
                length += 1
            return length

        l1_len = calculate_len(l1)
        l2_len = calculate_len(l2)

        if l1_len >= l2_len:
            longer = l1
            shorter = l2
        else:
            longer = l2
            shorter = l1

        dummy = longer

        while shorter:
            longer.val = longer.val + shorter.val
            if longer.val >= 10:
                longer.val -= 10
                if longer.next:
                    longer.next.val += 1
                else:
                    longer.next = ListNode(1)
            longer = longer.next
            shorter = shorter.next

        while longer:
            if longer.val >= 10:
                longer.val -= 10
                if longer.next:
                    longer.next.val += 1
                else:
                    longer.next = ListNode(1)
            longer = longer.next

        return dummy
