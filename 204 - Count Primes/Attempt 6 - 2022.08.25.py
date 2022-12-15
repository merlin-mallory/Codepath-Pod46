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
        1. Initialize an array of size n to True. This will represent all possible prime numbers, keyed to index value.
        2. Initialize index 0 and 1 to False, because they are special cases for prime numbers.
        3. The maximum size number that we'll need to check in the array is sqrt(n). So we'll loop from 2 to the
        floor of square root of n to confirm a prime number. When we find a prime number, we'll set all of the
        multiples of a prime number to False.
        4. After we've gone through the list, we can sum up the number of indexes remaining set to True in order to
        return the number of prime numbers for that given n.
        """
        import math

        prime_arr = [False, False] + [True] * (n-2)

        last_num = int(math.sqrt(n))
        for i in range(2, last_num+1):
            if prime_arr[i] is True:
                for j in range(i*i, len(prime_arr), i):
                    prime_arr[j] = False

        return sum(prime_arr)



result = Solution()
print(result.countPrimes(10))   # 4
print(result.countPrimes(0))    # 0
print(result.countPrimes(1))    # 0
print(result.countPrimes(5))    # 2
print(result.countPrimes(3))    # 1
