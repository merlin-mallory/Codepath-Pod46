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
        1. Create 2 vars, explore1 and explore2. Create list3.
        2. While explore1.next and explore2.next are not None
            3.  If explore1.val <= explore2.val
                4. list3.next = explore1
        I'm just going to write
        """
        # Failed attempt. I was close, but I think I should've just made new nodes containing copied values, instead of
        # actually reassign

        explore1, explore2 = list1, list2

        if explore1.val <= explore2.val:
            list3 = explore1
            list3.next = None
            explore1 = explore1.next
            dummy = list3
        else:
            list3 = explore2
            list3.next = None
            explore2 = explore2.next
            dummy = list3

        while explore1 is not None and explore2 is not None:
            if explore1.val <= explore2.val:
                list3.next = explore1
                list3.next.next = None
                list3 = list3.next
                explore1 = explore1.next
            elif explore1.val > explore2.val:
                list3.next = explore2
                list3.next.next = None
                list3 = list3.next
                explore2 = explore2.next

        if explore1:
            list3.next = explore1

        if explore2:
            list3.next = explore2

        return dummy
