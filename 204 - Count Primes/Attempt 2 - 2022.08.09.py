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
        1. Create a new array of size n^2, initialized to True.
        2. Loop from 2 to n, and step through the array, flipping multiples to false.
        3. Sum up and return the final answer
        """
        # Failed attempt. I was on the right track with the array allocation, but it was actually of size n,
        # instead of n^2. I needed to adjust for edge cases 0,1,and 2 because 0 and 1 are not prime numbers,
        # and although 2 is a prime number, the problem is looking for a count less than n. The outer loop goes from
        # 2 to sqrt(n)+1, and if the first slot of the outer loop is currently a prime number, then set multiples of
        # i to False.
        import math

        if n <= 2:
            return 0

        prime_arr = [False, False] + [True] * (n-2)

        for i in range(2, int(math.sqrt(n))+1):
            print(i)
            if prime_arr[i]:
                for j in range(i*i, n, i):
                    prime_arr[j] = False

        return sum(prime_arr)


result = Solution()
print(result.countPrimes(10))   # 4
print(result.countPrimes(0))    # 0
print(result.countPrimes(1))    # 0
