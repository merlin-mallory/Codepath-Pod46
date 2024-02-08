# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first
        two lists.

        Return the head of the merged linked list.

        Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Example 2:
        Input: list1 = [], list2 = []
        Output: []

        Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]

        Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

        Plan:
        Linked List
        Create a list3 pointer.
        Compare list1.val with list2.val. If list1.val < list2.val, then list3 = list1. Otherwise, list3 = list2.
        Loop while there is both list1 and list2.
            Set list3.next = the lesser of list1.val and list2.val.
            Advance both the list3 and the appropriate list1/list2 pointer.
        Eventually we'll break out of the loop when either list1 or list2 hits Null.
        If there are any nodes remaining, tack them onto list3
        Return dummy.next
        Time: O(n)
        Space: O(1)
        """
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val <= list2.val:
            list3 = list1
            list1 = list1.next
        else:
            list3 = list2
            list2 = list2.next

        dummy = list3

        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next
                list3 = list3.next
            else:
                list3.next = list2
                list2 = list2.next
                list3 = list3.next

        if list1:
            list3.next = list1

        if list2:
            list3.next = list2

        return dummy
