class Solution:
    def countPrimes(self, n: int) -> int:
        """
        https://leetcode.com/problems/count-primes/

        Given an integer n, return the number of prime numbers that are strictly less than n.

        Input: n = 10
        Output: 4
        Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

        Input: n = 0
        Output: 0

        Input: n = 1
        Output: 0

        Constraints:
        0 <= n <= 5 * 10^6

        Plan:
        1. Initialize a primes_array of size n to True. Each index corresponds to number in range n. True indicates
        that the function thinks the current index is a prime number. False indicates that it's not a prime number.
        2. Set the 0 and 1 indexes to False, because they are not prime numbers by special exception.
        3. Loop from 2 to the square root of n. We don't need to explore past the square root of n, because beyond
        that would exceed the range of the array. If primes_array[i] = True, then loop through all the multiples of i
        to the end of the array, and flip them to False.
        4. At the end of the loop, sum up the number of primes remaining in the array, and return the value.
        5. Time complexity: Outer loop is sqrt(n), inner loop is (n), so at first glance it looks like n*sqrt(n). But
        it actually might be better than that, because at each step we're cutting the number of prime numbers in the
        array by about half. So it might involve some kind of log(n) complexity instead.
        6. Space complexity: O(n)
        """
        import math
        if n <= 2:
            return 0

        primes_arr = [False, False] + [True] * (n-2)

        for i in range(2, int(math.sqrt(n)+1)):
            if primes_arr[i] == True:
                for j in range(i*i, len(primes_arr), i):
                    primes_arr[j] = False

        return sum(primes_arr)

result = Solution()
print(result.countPrimes(10))   # 4
print(result.countPrimes(0))    # 0
print(result.countPrimes(1))    # 0
print(result.countPrimes(5))    # 2
print(result.countPrimes(3))    # 1
