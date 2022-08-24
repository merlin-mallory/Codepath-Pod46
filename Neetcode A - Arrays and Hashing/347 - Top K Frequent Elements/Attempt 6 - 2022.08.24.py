import collections
import heapq


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
        1. Create a hashmap. Keys: nums[i], Values: frequency counts.
        2. Loop through nums, construct tuples containing (frequency counts, keys), and add them to max_heap.
        3. Pop k elements from the max_heap, and append them to the final_arr
        '''
        import collections

        final_arr = []

        hashmap = collections.defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1

        max_heap = []

        for key, value in hashmap.items():
            current_tup = (-value, key)
            heapq.heappush(max_heap, current_tup)

        for j in range(k):
            if max_heap:
                _, current_val = heapq.heappop(max_heap)
                final_arr.append(current_val)

        return final_arr
