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
        1. Make a hashmap. Keys: nums[i], Values: Current count of nums[i] in dictionary.
        2. Loop through nums and create the hashmap.
        3. Loop through the dictionary, create tuples containing (count, value), and add them to a maxheap.
        4. Pop k tuples from the max heap, and append them to the final array.
        5. This is nlogn because of the heap. Might as well sort it.
        '''
        import collections

        hashmap = collections.defaultdict(int)  # Keys: nums[i], Values: Count of all nums[i] in the dictionary
        for num in nums:
            hashmap[num] += 1

        max_heap = []

        for key in hashmap:
            current_tuple = (-hashmap.get(key), key)
            heapq.heappush(max_heap, current_tuple)  # Is the default max heap or min heap?

        final_arr = []

        for i in range(k):
            _, val = heapq.heappop(max_heap)
            final_arr.append(val)

        return final_arr
