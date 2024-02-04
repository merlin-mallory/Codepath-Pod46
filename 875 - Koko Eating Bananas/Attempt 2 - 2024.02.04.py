from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have
        gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats
        k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat
        any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

        Return the minimum integer k such that she can eat all the bananas within h hours.

        Example 1:
        Input: piles = [3,6,7,11], h = 8
        Output: 4

        Example 2:
        Input: piles = [30,11,23,4,20], h = 5
        Output: 30

        Example 3:
        Input: piles = [30,11,23,4,20], h = 6
        Output: 23

        Constraints:
        1 <= piles.length <= 10^4
        piles.length <= h <= 10^9
        1 <= piles[i] <= 10^9

        Plan:
        Binary Search
        1. Loop through piles and set max_complete_k = max(piles). Init min_k = max(piles).
        2. Do a binary search between 1 and max_complete_k. At each iteration, see if Koko can complete eating all
        the bananas in time successfuly. If success, then set l = m + 1. If fail, set r = m - 1. Update min_k.
        3. Return min_k.
        '''
        import math
        min_k = 0
        for i in range(len(piles)):
            if piles[i] > min_k:
                min_k = piles[i]

        l, r = 1, min_k
        while l < r:
            m = (l+r)//2
            time_to_finish = 0
            for i in range(len(piles)):
                time_to_finish += math.ceil(piles[i] / m)

            if time_to_finish <= h:
                r = m
            else:
                l = m + 1

        return r


result = Solution()
print(result.minEatingSpeed([3,6,7,11], 8))         # 4
print(result.minEatingSpeed([30,11,23,4,20], 5))    # 30
print(result.minEatingSpeed([30,11,23,4,20], 6))    # 23
print(result.minEatingSpeed([312884470],312884469)) # 2
