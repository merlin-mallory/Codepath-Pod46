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
        1. Create an empty merged_list.
        2. While list1.next is not None and list2.next is not None, compare the current values in both lists,
        add the lower value to the merged_list, and iterate that specific list by +1
        3. Eventually one of the lists will exhaust, and then we'll add all the remaining nodes of the opposite list
        to merged_list, until it also reaches a .next == None value.
        4. Return the merged LL
        """

        current_l1 = list1
        current_l2 = list2
        merged_list = ListNode()
        dummy = merged_list

        while current_l1 is not None and current_l2 is not None:
            if current_l1.val < current_l2.val:
                merged_list.next = ListNode(current_l1.val)
                current_l1 = current_l1.next
                merged_list = merged_list.next
            else:  # current_l1.val >= current_l2.val
                merged_list.next = ListNode(current_l2.val)
                current_l2 = current_l2.next
                merged_list = merged_list.next

        if current_l1 is not None:
            merged_list.next = current_l1

        if current_l2 is not None:
            merged_list.next = current_l2

        return dummy.next
