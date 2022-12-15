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

        Plan:
        1. Convert the LL to an array.
        2. Check the array for palindrome status, and return it
        3. Time: O(n), Space: O(n).
        """
        palin_arr = []
        current = head
        while current:
            palin_arr.append(current.val)
            current = current.next

        left, right = 0, len(palin_arr)-1
        while left < right:
            if palin_arr[left] != palin_arr[right]:
                return False
            left += 1
            right -= 1
        return True

        # return palin_arr == palin_arr[::-1]
