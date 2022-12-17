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
        1. Create nums_count_dict. Keys: Unique values in nums, Values: Count of that unique value.
        2. Get dict_keys.
        3. Create a freq_arr of size equal to the length of nums + 1
        4. Loop through dict_keys and append the value to the appropriate index in freq_arr.
        5. Create a final_arr.
        6. Loop backwards through freq_arr until the length of final_arr == k.
        7. Return final_arr.
        8. Time: O(n) to make dict_keys, freq_arr, final_arr. Space: O(n).
        '''
        from collections import defaultdict
        nums_count_dict = defaultdict(int)
        for num in nums:
            nums_count_dict[num] += 1

        freq_arr = [[] for _ in range(len(nums)+1)]

        for key, value in nums_count_dict.items():
            freq_arr[value].append(key)

        final_arr = []

        for i in range(len(freq_arr)-1, -1, -1):
            for j in range(len(freq_arr[i])):
                final_arr.append(freq_arr[i][j])
                if len(final_arr) == k:
                    return final_arr


answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)