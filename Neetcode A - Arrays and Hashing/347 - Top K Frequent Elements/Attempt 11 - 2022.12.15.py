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

        1. Create nums_count_dict. Key: unique values in nums, Values: count of the key's value.
        2. Loop through nums to create nums_count_dict.
        3. Create nums_freq_arr, of size equal to the length of nums + 1. Each index initialized to an empty list.
        4. Loop through nums_count_dict, and append the key to nums_freq_arr[value].
        5. Construct final_arr. Loop backwards through nums_freq_arr and collect the k most frequent elements.
        6. Time: O(n), Space: O(n).
        '''
        from collections import defaultdict
        nums_count_dict = defaultdict(int)
        for num in nums:
            nums_count_dict[num] += 1

        nums_freq_arr = [[] for _ in range(len(nums)+1)]
        for key, value in nums_count_dict.items():
            nums_freq_arr[value].append(key)

        final_arr = []

        for i in range(len(nums_freq_arr)-1, 0, -1):
            for j in range(len(nums_freq_arr[i])):
                final_arr.append(nums_freq_arr[i][j])
                if len(final_arr) == k:
                    return final_arr

# Neetcode
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