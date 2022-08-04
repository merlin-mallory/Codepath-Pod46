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

        1. The upper bound of n is pretty high, so we can't brute force it. There's probably some mathematical way to
        generate prime numbers, and we just need to count the number of generations up to n.
        """
        # Didn't bother attempting. It turns out the trick is allocating an n size array that will contain booleans
        # where False indicates non-primes, and True indicates primes. The initial array [0] and [1] index are
        # initialized to False, but the rest of the indexes are initialized to True. Then we loop from 2 to the sqrt(
        # n)+1 (we don't need to loop beyond sqrt(n) because those would be non-primes. If is_prime_arr[i] is True,
        # then set all multiples of i to False. And then at the very end, return sum(is_prime_arr), which will return
        # the total number of prime numbers faster than a normal loop.

        if n <= 2:
            return 0

            # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
            # Initialze numbers[2] through numbers[n-1] as True because we assume each number
            # is prime until we find a prime number (p) that is a divisor of the number
        numbers = [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        # numbers[index] will only be true where index is a prime number
        # return the number of indices whose value is true.
        return sum(numbers)


result = Solution()
print(result.countPrimes(10))  # 4
print(result.countPrimes(0))  # 0
print(result.countPrimes(1))  # 0
