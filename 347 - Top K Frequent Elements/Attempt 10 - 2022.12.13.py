class Solution:
    def topKFrequent(self, nums, k):
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
        1. Loop through nums and construct nums_count_dict. Keys: unique nums[i], Values: count of that unique value.
        2. Calculate the number of unique keys in the nums_count_dict, and create a bucket_arr of a size equal to
        that length+1. Each index in bucket_arr will be initialized to an empty list.
        3. Loop through the keys in nums, and append each value to the appropriate bucket.
        4. Loop backwards through the bucket list k times, and construct the final return arr.
        5. Return the final return arr.
        6. Time complexity: O(n) to make the dict, parse the dict, make bucket_arr, make the final return arr.
        7. Space complexity: O(n) to make the dict, bucket arr, final return arr.
        '''
        from collections import defaultdict
        nums_count_dict = defaultdict(int)
        # Keys: Unique nums[i], Values: Current count of that key in the dict

        for i in range(len(nums)):
            nums_count_dict[nums[i]] += 1

        list_of_keys = list(nums_count_dict.keys())
        length_of_keys = len(list_of_keys)

        bucket_arr = [[] for x in range(length_of_keys+2)]

        for j in range(len(list_of_keys)):
            current_count = nums_count_dict.get(list_of_keys[j])
            bucket_arr[current_count].append(list_of_keys[j])

        res = []
        current_index = len(bucket_arr) -1
        while len(res) < k:
            if bucket_arr[current_index] == []:
                current_index -= 1
                continue
            else:
                for l in range(len(bucket_arr[current_index])):
                    res.append(bucket_arr[current_index][l])
                    if len(res) == k:
                        return res
                current_index -= 1

answer = Solution()
result = answer.topKFrequent([1,1,1,2,2,3], 2) # [1,2]
print(result)

result2 = answer.topKFrequent([1], 1)  # [1]
print(result2)