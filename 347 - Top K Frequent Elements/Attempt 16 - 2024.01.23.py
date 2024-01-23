from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        https://leetcode.com/problems/top-k-frequent-elements/

        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer
        in any order.

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Input: nums = [1], k = 1
        Output: [1]

        Constraints:

        1 <= nums.length <= 10^5
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.

        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

        Plan:
        Heap
        1. Create counts dict. Keys: Number in nums, Values: Count of the key
        2. Loop through nums, construct tuples, toss into minheap, and if the heap exceeds k, then pop and discard.
        3. Empty out the heap and construct and return the final_arr.
        '''
        final_arr = []

        import collections
        import heapq

        counts = collections.Counter(nums)

        minheap = []

        for key, value in counts.items():
            current_tup = (value, key)
            heapq.heappush(minheap, current_tup)
            if len(minheap) > k:
                heapq.heappop(minheap)

        while minheap:
            _, current_val = heapq.heappop(minheap)
            final_arr.append(current_val)

        return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)