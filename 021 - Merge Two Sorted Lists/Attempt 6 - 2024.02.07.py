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
        1. Determine which list is shorter by iterating through them. Set shorter_list = shorter len, and
        longer_list = longer len.
        2. Loop until the end of the shorter list.
            3. Compare the values in list1 and list2. Set list3.next to the shorter one, and keep advancing.
        4. Tack on the remaining elements in the larger list by setting the .next to the remainder.
        5. Return list3.
        Time: O(n)
        Space: O(1)
        Edge: 0 nodes
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
            if list1.val < list2.val:
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
