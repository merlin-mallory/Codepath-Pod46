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
        1. I think it will be easier to eliminate the numbers that are not prime, and then count up the remaining
        prime numbers.
        2. Create primes_arr of size(n). Initialize all indexes to True (currently non prime). Set index 0 and 1 to
        False, because they are not prime numbers by definition. 2 is a prime number, but in this function we're
        looking for prime numbers less than n, so we'll leave it set to 2.
        3. Note that n could potentially have 0 data, so we need to adjust for direct indexing.
        4. We know that we only need to explore the square root of n entries in the primes_arr, because any square is
        going to be not a prime number. So maybe outer loop sqrt(n). This will find an index that is not a prime
        number, set it to False, and then we need to do an inner loop to set all of the multiples of that number to
        False.
        5. However in order to keep the time complexity down, we want to make sure that we don't double-loop over any
        entry, so we want to go through the loop once to find multiples of 2, and then once to find multiples of 3,
        but we don't want to loop through multiples of 6. So we need to add a check to see if the initial index is
        set to False, and if it is, then skip the looping process.
        """
        import math
        if n <= 2:
            return 0

        primes_arr = [False, False] + [True] * (n-2)
        for i in range(2, int(math.sqrt(n))+1):
            if primes_arr[i] is True:
                for j in range(i*i, len(primes_arr), i):
                    primes_arr[j] = False

        return sum(primes_arr)

result = Solution()
print(result.countPrimes(10))   # 4
print(result.countPrimes(0))    # 0
print(result.countPrimes(1))    # 0
print(result.countPrimes(5))    # 2
print(result.countPrimes(3))    # 1
