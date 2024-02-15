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

        Create merged_lists.
        Loop until the len of lists is 1 (not including the first iteration).
            Loop through lists, grab 2 lists at a time, merge them, and put the result in merged_lists. If there's
            only 1, then merge the 1 with Null.
        Set lists to mergedlists.
        Return lists[0]

        Time: O(n log n)
        Space: O(1)
        Edge: Possible to be 0 len lists.
        '''
        if not lists:
            return None
        if len(lists) == 0:
            return None

        def mergeSort(list1, list2):
            dummy = ListNode(-1)
            list3 = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    list3.next = list1
                    list1 = list1.next
                else:
                    list3.next = list2
                    list2 = list2.next
                list3 = list3.next
            if list1:
                list3.next = list1
            if list2:
                list3.next = list2
            return dummy.next

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                list3 = mergeSort(list1, list2)
                merged_lists.append(list3)
            lists = merged_lists

        return lists[0]

