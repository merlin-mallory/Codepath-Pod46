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
        Linked List Traversal
        Time: O(n)
        Space: O(n)
        Edge: k could be 0, lists could be empty
        '''
        if not lists: return
        def mergeSort(n1,n2):
            dummy = ListNode(-1)
            n3 = dummy
            while n1 and n2:
                if n1.val <= n2.val:
                    n3.next = n1
                    n1 = n1.next
                else:
                    n3.next = n2
                    n2 = n2.next
                n3 = n3.next
            if n1: n3.next = n1
            elif n2: n3.next = n2
            return dummy.next
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                l3 = mergeSort(l1, l2)
                temp.append(l3)
            lists = temp
        return lists[0]

