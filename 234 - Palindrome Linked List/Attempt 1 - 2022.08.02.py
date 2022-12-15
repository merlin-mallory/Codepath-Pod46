# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        https://leetcode.com/problems/palindrome-linked-list/

        Given the head of a singly linked list, return true if it is a palindrome.

        Input: head = [1,2,2,1]
        Output: true

        Input: head = [1,2]
        Output: false

        Constraints:
        The number of nodes in the list is in the range [1, 10^5].
        0 <= Node.val <= 9

        Plan 1:
        1. Create a new LL, and reverse the head.
        2. Iterate through the original LL and the new LL, and if there is a value mismatch, return False. If we
        reach the end of the list (.next is None) without returning False, then we've found a palindrome,
        so return true.
        3. Time: O(2n), Space: O(n)

        Plan 2:
        1. Calculate the len of the LL.
        2. Create a stack, and loop to the halfway point, adding each element to the stack. Then loop to the end of
        the LL, popping a element from the stack each iteration, and verifying that the stack's value == the current
        node's value. If there's ever a mismatch, then return False. Otherwise return true.
        3. Time: O(2n), Space: O(n/2)

        Not sure what the O(n) time and O(1) space solution is.
        """
        # Here's the optimal O(n) time and O(1) space solution, reversing the second half in-place with the two
        # runners technique. The two runners technique returns the midpoint in O(n/2) time. Then we take that
        # midpoint, and reverse the midpoint.next LL.

    #     if head is None:
    #         return True
    #
    #     # Find the end of first half and reverse second half.
    #     first_half_end = self.end_of_first_half(head)
    #     second_half_start = self.reverse_list(first_half_end.next)
    #
    #     # Check whether or not there's a palindrome.
    #     result = True
    #     first_position = head
    #     second_position = second_half_start
    #     while result and second_position is not None:
    #         if first_position.val != second_position.val:
    #             result = False
    #         first_position = first_position.next
    #         second_position = second_position.next
    #
    #     # Restore the list and return the result.
    #     first_half_end.next = self.reverse_list(second_half_start)
    #     return result
    #
    # def end_of_first_half(self, head):
    #     fast = head
    #     slow = head
    #     while fast.next is not None and fast.next.next is not None:
    #         fast = fast.next.next
    #         slow = slow.next
    #     return slow
    #
    # def reverse_list(self, head):
    #     previous = None
    #     current = head
    #     while current is not None:
    #         next_node = current.next
    #         current.next = previous
    #         previous = current
    #         current = next_node
    #     return previous

    # Alternatively, we could simply convert the LL to an array, and then use the two pointer technique to check for
    # the palindrome.

        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
