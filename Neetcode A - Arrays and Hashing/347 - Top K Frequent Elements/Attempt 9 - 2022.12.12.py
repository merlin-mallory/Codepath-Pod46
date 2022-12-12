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

        1. Create nums_count_dict. Keys: nums[i], Values: Count of that value in nums.
        2. Loop through nums, and construct nums_count_dict.
        3. Create nums_heap.
        4. Loop through nums_count_dict, and add each [nums_count, nums_val] to the heap.
        5. Create res_arr.
        6. Loop k times through nums_heap, and pop k nums_val, and append them to res_arr.
        7. Return res_arr.
        8. Time: O(n) to create the dict, O(m log m) to create the heap (where m is the number of unique elements),
        O(k) to create and return the final list. Overall time complexity: O(m log m).
        9. Space: O(n) for the dict, O(m) for the heap
        '''
        from collections import defaultdict
        import heapq

        nums_count_dict = defaultdict(int)
        # Keys: unique nums[i], Values: Count of that unique key so far in the dict.
        for i in range(len(nums)):
            nums_count_dict[nums[i]] += 1

        nums_heap = []
        for key, count in nums_count_dict.items():
            current_tup = (-count, key)
            heapq.heappush(nums_heap, current_tup)

        res = []
        for j in range(k):
            _, current_val = heapq.heappop(nums_heap)
            res.append(current_val)

        return res

        # Heap works, but it's actually n(log(k)).
        # There is a O(n) solution using bucket sort

        # count = {}
        # freq = [[] for i in range(len(nums) + 1)]
        #
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        # for n, c in count.items():
        #     freq[c].append(n)
        #
        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res


