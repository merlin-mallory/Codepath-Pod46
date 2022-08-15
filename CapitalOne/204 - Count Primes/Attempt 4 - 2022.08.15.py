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
        1. I think the easiest way to calculate this is start with an array of size n initialized to True,
        and then loop through multiples and set those to False. We will only need to loop through sqrt(n) multiples.
        After that we can sum up the number of indexes remaining that are still set to True.
        """
        import math

        if n < 2:
            return 0

        prime_arr = [False, False] + [True] * (n-2)
        for i in range(2, int(math.sqrt(n))+1):
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
