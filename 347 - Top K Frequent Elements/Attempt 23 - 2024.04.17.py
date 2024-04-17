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
        Maxheap
        Time: O(n log k), where k is the number of unique elements in nums
        Space: O(n)
        Edge: None
        '''
        import collections, heapq
        nums_dict = collections.Counter(nums)
        max_heap = []
        for key, val in nums_dict.items():
            heapq.heappush(max_heap, [-val, key])
        final_arr = []
        while len(final_arr) < k:
            _, key = heapq.heappop(max_heap)
            final_arr.append(key)
        return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)