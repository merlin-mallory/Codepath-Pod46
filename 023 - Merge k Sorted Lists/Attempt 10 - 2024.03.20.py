# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        023 - Merge k Sorted Lists

        https://leetcode.com/problems/merge-k-sorted-lists/

        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6

        Example 2:
        Input: lists = []
        Output: []

        Example 3:
        Input: lists = [[]]
        Output: []

        Constraints:
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 10^4.

        Plan:
        Linked List
        Create mergeSort function. Takes l1 and l2, returns the sorted l3.
        Loop while len(lists) > 1.
            merged_lists = []
            Loop in step 2 to end of lists.
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                l3 = mergeSort(l1,l2)
                merged_lists.append(l3)
            lists = merged_lists
        Return lists[0]
        Time: O(n log n)
        Space: O(1)
        Edge: Could be 0 len lists
        '''
        def mergeSort(l1, l2):
            dummy = ListNode(-1)
            l3 = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next
            if l1: l3.next = l1
            if l2: l3.next = l2
            return dummy.next
        if len(lists) == 0: return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                l3 = mergeSort(l1, l2)
                merged_lists.append(l3)
            lists = merged_lists
        return lists[0]


