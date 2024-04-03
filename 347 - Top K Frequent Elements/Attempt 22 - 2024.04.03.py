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
        Time: O(n log k)
        Space: O(k)
        Edge: None
        '''
        import collections, heapq
        nums_dict = collections.Counter(nums)
        nums_heap = []
        for key, value in nums_dict.items():
            heapq.heappush(nums_heap, [value, key])
            if len(nums_heap) > k:
                heapq.heappop(nums_heap)
        final_arr = []
        for value, key in nums_heap:
            final_arr.append(key)
        return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)