# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
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
        """
        final_arr = []
        while head is not None:
            final_arr.append(head.val)
            head = head.next
        return final_arr == final_arr[::-1]
