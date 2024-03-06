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
        Create minheap.
        Loop through nums
            Append nums[i] to minheap
            If len(minheap) > k, pop from minheap and discard.
        Return minheap
        Time: O(n * log k)
        Space: O(1) or O(n), depending upon the output array counting
        Edge: None
        '''
        import heapq, collections
        min_heap = []
        nums_count = collections.Counter(nums)
        final_arr = []
        for key, value in nums_count.items():
            heapq.heappush(min_heap, [value, key])
            if min_heap and (len(min_heap) > k):
                heapq.heappop(min_heap)
        for _, value in min_heap:
            final_arr.append(value)
        return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)