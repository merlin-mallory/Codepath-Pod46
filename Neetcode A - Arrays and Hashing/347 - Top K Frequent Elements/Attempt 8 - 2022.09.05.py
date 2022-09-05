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
        '''
        import collections, heapq
        mapping_dict = collections.defaultdict(int)
        max_heap = []
        final_arr = []

        for i in range(len(nums)):
            mapping_dict[nums[i]] += 1

        for key in mapping_dict:
            heapq.heappush(max_heap, (-mapping_dict.get(key), key))

        for j in range(k):
            if max_heap:
                _, val = heapq.heappop(max_heap)
                final_arr.append(val)

        return final_arr
