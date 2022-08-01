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
        1. Create a max_heap.
        2. Sort the nums.
        3. Loop through nums until the value changes, then add a tuple containing (count, value) to the max_heap,
        continue until reaching the end of nums.
        4. Pop k tuples from the max_heap and append them to the final array.
        '''
        nums.sort()

        current_val = nums[0]
        current_count = 1

        max_heap = []
        heapq.heapify(max_heap)

        for i in range(1, len(nums)):
            if nums[i] == current_val:
                current_count += 1
            else:
                heapq.heappush(max_heap, (-current_count, current_val))
                current_val = nums[i]
                current_count = 1
        heapq.heappush(max_heap, (-current_count, current_val))

        print(max_heap)

        final_arr = []

        for i in range(k):
            my_count, my_val = heapq.heappop(max_heap)
            print(my_count, my_val)
            final_arr.append(my_val)

        return final_arr
