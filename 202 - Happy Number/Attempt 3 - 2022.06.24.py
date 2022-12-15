class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        https://leetcode.com/problems/happy-number/description/
        Write an algorithm to determine if a number n is happy.

        A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the
        process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not
        include 1. Those numbers for which this process ends in 1 are happy. Return true if n is a happy number,
        and false if not.

        Input: n = 19
        Output: true
        Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

        Input: n = 2
        Output: false

        Constraints:
        1 <= n <= 2^31 - 1

        1. It looks like we need to take of two situations. If the cycle loops to 1, then we should return true. And
        if it doesn't, then it should return False.
        2. So its kinda like we're checking for a cycle in a linked list. This is not actually a linked list,
        we're just simulating it.
        3. The best way that I can think of to find a cycle in a linked list is to use the fast/slow pointer method.
        If the fast pointer == slow pointer, then we break the loop. If the value it breaks at is 1, then we return
        True. Otherwise, we return False.
        4. We don't need to worry about infinite increasing numbers because there is a maximum of 8 * len(n)
        possibilities for the remainders.
        '''

        def calc_next_sum(num):
            new_sum = 0
            str_num = str(num)
            for char in str_num:
                new_sum = new_sum + int(char) ** 2
            return new_sum

        slow_pointer = n
        fast_pointer = calc_next_sum(n)

        while fast_pointer != 1 and fast_pointer != slow_pointer:
            slow_pointer = calc_next_sum(slow_pointer)
            fast_pointer = calc_next_sum(calc_next_sum(fast_pointer))

        return fast_pointer == 1
