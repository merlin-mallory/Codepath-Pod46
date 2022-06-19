# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]

        N is in range 1-100
        Node.val are only digits 0-9
        There are no leading zeros

        Plan 1:

        1. Create strings to represent both lists.
        2. Loop through each linked list and concatenate the results
        3. Convert both strings to integers
        4. Calculate the sum
        5. Create a new linked list

        Plan 2:
        1. Calculate the length of both linked lists
        2. Add the smaller list's values to the bigger list's values, carrying ones as necessary
        3. If the final digit of the larger list carries, then we need to add an extra node.
        '''


        def calculate_len(ll):
            if not ll:
                return 0

            counter = 1
            current = ll
            while current.next is not None:
                counter += 1
                current = current.next
            return counter


        l1_len = calculate_len(l1)
        l2_len = calculate_len(l2)

        if l1_len >= l2_len:
            longer_ll = l1
            shorter_ll = l2
        else:
            longer_ll = l2
            shorter_ll = l1

        longer_head = longer_ll
        current_longer = longer_ll
        current_shorter = shorter_ll

        while current_shorter is not None:
            current_longer.val = current_longer.val + current_shorter.val
            if current_longer.val >= 10:
                current_longer.val -= 10
                if current_longer.next is not None:
                    current_longer.next.val += 1
                else:
                    current_longer.next = ListNode(1)
            current_longer = current_longer.next
            current_shorter = current_shorter.next

        while current_longer is not None:
            if current_longer.val >= 10:
                current_longer.val -= 10
                if current_longer.next is not None:
                    current_longer.next.val += 1
                else:
                    current_longer.next = ListNode(1)
            current_longer = current_longer.next

        return longer_head
