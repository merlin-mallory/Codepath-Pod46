class Solution:
    def isHappy(self, n: int) -> bool:
        '''
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

        Plan 1:
        1. We need to account for 3 scenarios: Number reaches 1, number cycles, or number goes up to infinity.
        2. But we don't need to worry about the infinity situation, because a digit has a maximum of 9^2 = 81
        possiblities. So a 2^31 digit string has 81 * 2^31 possibilities, which is a constant multiplier. In
        addition, if we reach 1, then it will also cycle because 1^2 will always be 1. So we just need to find if the
        cycle happens at 1, or some other number.
        3. So we need some way to detect cycles and 1. We could use hashmaps, or an implicit linked list.
        4. Hashmap would require more space, so we will go with the implicit linked list.
        5. Make a check_next function, which will take a number and return the sum of the squares.
        6. Create 2 linked lists: slow_runner and fast_runner (starts one call ahead of the slow_runner)
        7. While the fast_runner != 1 and slow_runner != fast_runner
            8. slow_runner = check_next(slow_runner)
            9. fast_runner = check_next(check_next(fast_runner)
        10. At some point one of the loop conditions will break, and if fast_runner = 1, then return True. Otherwise,
        return False.
        '''

        def check_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = check_next(n)

        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = check_next(slow_runner)
            fast_runner = check_next(check_next(fast_runner))

        return fast_runner == 1