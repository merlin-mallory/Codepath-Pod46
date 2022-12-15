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
        1. Loop through nums and create a counts_dict. Keys: unique nums[i] values. Value: Frequency count.
        2. Create a max_heap. Loop through counts_dict and add a tuple containing (count, unique_value) to the max_heap.
        3. Pop k tuple from the max heap, and append them to the final array.
        4. Return the final array.

        Alt:
        Pythonic way to simply sort by frequency? And then iterate until k unique values have been seen.
        '''
        import collections
        counts_dict = collections.defaultdict(int)
        for i in range(len(nums)):
            counts_dict[nums[i]] += 1

        max_heap = []

        for key in counts_dict.keys():
            current_tup = (-1 * counts_dict.get(key), key)
            heapq.heappush(max_heap, current_tup)

        final_arr = []
        for j in range(k):
            if max_heap:
                _, current_val = heapq.heappop(max_heap)
                final_arr.append(current_val)

        return final_arr


