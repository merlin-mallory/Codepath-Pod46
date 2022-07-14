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
        1. Create a counts_dict. Keys: nums[i], values: frequency of nums[i] in the array, as a counter
        2. Create a max_heap. Loop through counts dict and add tuples (count, ele).
        3. Pop k tuples from the max_heap, deconstruct, and append the eles to the final array.
        '''
        import collections
        counts_dict = collections.defaultdict(int)
        max_heap = []

        for num in nums:
            counts_dict[num] += 1

        for key in counts_dict:
            max_heap.append((-1*counts_dict.get(key), key))

        heapq.heapify(max_heap)

        final_arr = []
        for i in range(k):
            _, ele = heapq.heappop(max_heap)
            final_arr.append(ele)

        return final_arr
