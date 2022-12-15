import collections


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
        1. Create ele_count_dict. Keys: nums[i], Values: Counter containing the frequency of the int in the list
        2. Loop through nums and fill up the ele_count_dict.
        3. Loop the ele_count_dict's keys, and construct tuples containing (count, value), and append them to the
        final_list.
        4. Sort the final_list, and the loop through the final list in range k, appending each value to the
        grand_final_array.
        4. Return the grand_final_array.
        5. Time: O(n log n), Space: O(n^2)

        Alt: Maybe use a heap instead of sorting
        '''

        ele_count_dict = collections.defaultdict(int) # Keys: nums[i], Values: Key's frequency so far(int)
        for ele in nums:
            ele_count_dict[ele] += 1

        final_list = []

        for key in ele_count_dict.keys():
            this_tup = (ele_count_dict.get(key), key)
            final_list.append(this_tup)

        final_list.sort(reverse=True)

        grand_final_list = []
        for i in range(k):
            grand_final_list.append(final_list[i][1])

        return grand_final_list

# We can use a heap to improve the space complexity, but time complexity would remain the same.

# Bucketsort O(n) time O(n) space solution
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]
#
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)
#
#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res
#
#         # O(n)
