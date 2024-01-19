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
        Hashmap
        1. Create a dict. Keys: nums[i], Values: Count of nums[i] in dict.
        2. Create a min_heap.
        3. Loop through dict. Construct a tuple (value, key) on each iteration, and add it to the heap. Whenever the
        length of the heap exceeds k, pop and discard the top of the min_heap.
        4. Loop through the heap. Pop every tuple, deconstruct the value, and append to the final_arr.
        5. Return the final_arr
        '''
        import collections
        import heapq

        final_arr =[]

        dict = collections.defaultdict(int)
        for i in range(len(nums)):
            dict[nums[i]] += 1

        min_heap = []

        for key, value in dict.items():
            current_tup = (value, key)
            heapq.heappush(min_heap, current_tup)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        while min_heap:
            _, key = heapq.heappop(min_heap)
            final_arr.append(key)

        return final_arr





answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)