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
        1. Sort the array, and initialize the heap, and the final_arr.
        2. Loop through the array. Construct a tuple (-frequency, value). Add it to the heap. Using the negative
        makes it operate as a maxheap instead of a minheap.
        3. Pop k tuples from the heap, and append them to final arr.
        4. Return final_arr
        Time: O(n log n), Space: O(n)
        '''
        if not nums:
            return []

        import heapq
        import collections

        dict = collections.defaultdict(int)
        final_arr = []
        heap = []

        for i in range(len(nums)):
            dict[nums[i]] += 1

        for key, value in dict.items():
            current_tup = (value, key)
            heapq.heappush(heap, current_tup)
            if len(heap) > k:
                heapq.heappop(heap)

        while heap and k > 0:
            _, current_val = heapq.heappop(heap)
            final_arr.append(current_val)
            k -= 1

        return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)