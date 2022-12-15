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

        Plan:
        1. Convert the LL to an array
        2. Use 2 pointers to verify palindrome status.
        """
        # I implemented this pretty well, however I forgot to increment and decrement the pointers on the first
        # submission.

        pal_arr = []
        current_node = head

        while current_node is not None:
            pal_arr.append(current_node.val)
            current_node = current_node.next

        print("arr after LL:", pal_arr)

        left_pointer, right_pointer = 0, len(pal_arr)-1

        while left_pointer < right_pointer:
            if pal_arr[left_pointer] != pal_arr[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True
