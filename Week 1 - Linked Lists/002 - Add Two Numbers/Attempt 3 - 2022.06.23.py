# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/add-two-numbers/
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
        1. Loop through both lists and concatenate the values into strings.
        2. Convert the strings into integers
        3. Add the two ints together
        4. Create a new LL using the result
        5. Time: O(n), Space: O(n)

        Plan 2:
        1. Calculate the length of both strings.
        2. Loop through the shorter string, and add the shorter string's values to the longer strings value. If the
        value exceeds 10, then subtract ten from the current value. If there is a next value, add +1 to the next
        value. Otherwise, make a new node with a 1 value.
        3. Return the longer LL
        4. Time: O(m+n), where m = length of longer string, and n = length of shorter string.
        5. Space: O(1), no new data structures

        I will try plan 2
        '''

        def calculate_len(node):
            if not node:
                return 0
            counter = 1
            while node.next:
                counter += 1
                node = node.next
            return counter

        l1_len = calculate_len(l1)
        l2_len = calculate_len(l2)

        if l1_len >= l2_len:
            longer_LL = l1
            shorter_LL = l2
        else:
            longer_LL = l2
            shorter_LL = l1

        dummy = ListNode(-1)
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
