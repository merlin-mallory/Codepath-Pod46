class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        202 Happy Number: https://leetcode.com/problems/happy-number/

        Definition:
        A happy number is a number that can be reduced to 1 by continuously squaring its digits.
        If the number cycles, then the number is not happy.

        Input: n = 19
        Work: 1^2 + 9^2 = 82. 8^2 + 2^2 = 68. 6^2 + 8^2 = 100. 1^2 + 0^2 + 0^2 = 1.
        Output: True

        Input: n = 2
        Work: 2^2 = 4. 4^2 = 16. 1^2 + 6^2 = 37 ....
        Output: False

        Plan:
        Fast/slow pointer method?
        '''

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
