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
        1. Create a hashmap. Keys: nums[i] values, Values: Frequency count of that number.
        2. Loop through nums and construct the hashmap.
        3. Loop through the hashmap, and construct tuples (frequeuncy_count, value), and add them to a max_heap.
        4. Pop k tuples from the max_heap and append them to the final_arr.
        5. Return the final_arr
        '''
        import collections
        hashmap = collections.defaultdict(int)  # Keys: Unique values in nums, Values: Frequency count of unique value
        for num in nums:
            hashmap[num] += 1

        max_heap = []

        for key, value in hashmap.items():
            heapq.heappush(max_heap, (-value, key))

        final_arr = []

        for i in range(k):
            _, this_val = heapq.heappop(max_heap)
            final_arr.append(this_val)

        return final_arr
