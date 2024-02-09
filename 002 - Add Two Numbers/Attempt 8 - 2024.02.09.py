from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(elements: List[int]) -> Optional[ListNode]:
    """
    Convert an array of elements into a linked list and return the head of the list.
    """
    head = None
    current = None
    for element in elements:
        if not head:
            head = ListNode(element)
            current = head
        else:
            current.next = ListNode(element)
            current = current.next
    return head


def print_list(head: Optional[ListNode]) -> None:
    """
    Print the elements of a linked list.
    """
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


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
        Linked List
        1. Create an array.
        2. Loop through l1 and append each val as a string to the array.
        3. Join the array and convert to int.
        4. Repeat for l2
        5. Calculate desired_num
        6. Create l3 pointer
        7. Convert desired_num to str
        8. Flesh out l3.
        '''
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


solution = Solution()
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])
result = solution.addTwoNumbers(l1, l2)
print_list(result)  # Expected: [7,0,8]

l1 = create_list([0])
l2 = create_list([0])
result = solution.addTwoNumbers(l1, l2)
print_list(result)  # Expected: [0]

l1 = create_list([9,9,9,9,9,9,9])
l2 = create_list([9,9,9,9])
result = solution.addTwoNumbers(l1, l2)
print_list(result)  # Expected: [8,9,9,9,0,0,0,1]
