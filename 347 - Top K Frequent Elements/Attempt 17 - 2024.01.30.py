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
        1. Create nums_counts dict. Keys: Unique integers in nums, Values: Count of keys in nums.
        2. Loop through nums_counts, create tuples with (count, key), and toss into a minheap. Whenever the size of
        the minheap exceeds k, pop and discard the minimum value.
        3. After the loop completes, empty out the heap, deconstruct the tuples to get the keys, and append to the
        final_arr.
        4. Return the final_arr
        Edge Cases: None
        Time: O(n)
        Space: O(n)
        '''
        import collections
        import heapq
        nums_counts = collections.Counter(nums)
        final_arr = []
        minheap = []

        for key, value in nums_counts.items():
            current_tup = (value, key)
            heapq.heappush(minheap, current_tup)
            if len(minheap) > k:
                heapq.heappop(minheap)

        while minheap:
            _, cur_val = heapq.heappop(minheap)
            final_arr.append(cur_val)

        return final_arr




answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)