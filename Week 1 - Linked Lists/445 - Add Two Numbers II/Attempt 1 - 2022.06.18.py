# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         '''
#
#         Input: l1 = [7,2,4,3], l2 = [5,6,4]
#         Output: [7,8,0,7]
#
#         Input: l1 = [2,4,3], l2 = [5,6,4]
#         Output: [8,0,7]
#
#         Input: l1 = [0], l2 = [0]
#         Output: [0]
#
#         Constraints:
#
#         The number of nodes in each linked list is in the range [1, 100].
#         0 <= Node.val <= 9
#         It is guaranteed that the list represents a number that does not have leading zeros.
#
#         Plan:
#         1. Calculate the lengths of both lists.
#         2. Calculate the difference between the lengths of both lists.
#         3. Iterate through the longer length list until it reaches the difference.
#         4. Loop through both lists, adding the shorter list's value to the longer list's value.
#            Keep track of the previous node, and if the sum >= 10, then sum -=10, and the previous
#            node's val +1.
#         5. Loop through the longer list (n-m) times, in order to ensure that everything is carried
#            properly.
#         6. If the head of the longer list is >= 10, then create a new node(1).
#         7. Time: O(m+n + (m-n)^2), where m = len(longer_list), and n = len(shorter_list)
#         '''
#
#         def calculate_len(node):
#             len_counter = 0
#             while node:
#                 len_counter += 1
#                 node = node.next
#             return len_counter
#
#         l1_len = calculate_len(l1)
#         l2_len = calculate_len(l2)
#
#         if l1_len >= l2_len:
#             longer_list = l1
#             shorter_list = l2
#             m = l1_len
#             n = l2_len
#         else:
#             longer_list = l2
#             shorter_list = l1
#             m = l2_len
#             n = l1_len
#
#         len_diff = m-n
#         longer_list_prev = None
#
#         dummy = ListNode(-1)
#         dummy.next = longer_list
#
#         for i in range(len_diff):
#             longer_list_prev = longer_list
#             longer_list = longer_list.next
#
#         while longer_list:
#             longer_list.val += shorter_list.val
#             if longer_list.val >= 10:
#                 longer_list.val -= 10
#                 if longer_list_prev is not None:
#                     longer_list_prev.val += 1
#                 else:
#                     extra_node = ListNode(1)
#                     extra_node.next = longer_list
#                     dummy.next = extra_node
#
#             longer_list_prev = longer_list
#
#             longer_list = longer_list.next
#             shorter_list = shorter_list.next
#
#         for i in range(len_diff):
#             longer_list_prev = None
#             longer_list = dummy.next
#             for j in range(len_diff):
#                 if longer_list.val >= 10:
#                     longer_list.val -= 10
#                     if longer_list_prev is not None:
#                         longer_list_prev.val += 1
#                     else:
#                         extra_node = ListNode(1)
#                         extra_node.next = longer_list
#                         dummy.next = extra_node
#
#                 longer_list_prev = longer_list
#                 longer_list = longer_list.next
#
#         return dummy.next

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]


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

        Plan:
        1. Reverse both lists, so the units line up
        2. Initalize result_list = None and carry = 0.
        3. Loop through l1 and l2 until we reach both ends.
            4. If l1, x1 = l1.val, else x1 = 0
            5. If l2, x2 = l2.val, else x2 = 0
            6. Calculate the current_value = (carry + x1 + x2) % 10.
            7. Calculate the current_carry = (carry + x1 + x2) // 10
            8. Create a node with the current_value, and add it to the front of the result_list.
            9. Move the result_list to point to the current_value node.
            10. Iterate both l1 and l2 until they reach None.
        11. If there's a carry leftover, create a new node with the carry's value, set the newnode's.next to the head,
            and move the head to the new node.
        '''

        def reverse_list(head):
            last = None
            while head:
                temp = head.next
                head.next = last
                last = head
                head = temp
            return last