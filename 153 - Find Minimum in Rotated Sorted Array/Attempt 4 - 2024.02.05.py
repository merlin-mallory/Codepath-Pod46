from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        153 - Find Minimum in Rotated Sorted Array

        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
        the array nums = [0,1,2,4,5,6,7] might become:

        [4,5,6,7,0,1,2] if it was rotated 4 times. [0,1,2,4,5,6,7] if it was rotated 7 times. Notice that rotating an
        array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.

        Input: nums = [3,4,5,1,2]
        Output: 1
        Explanation: The original array was [1,2,3,4,5] rotated 3 times.

        Input: nums = [4,5,6,7,0,1,2]
        Output: 0
        Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

        Input: nums = [11,13,15,17]
        Output: 11
        Explanation: The original array was [11,13,15,17] and it was rotated 4 times.

        Constraints:
        n == nums.length
        1 <= n <= 5000
        -5000 <= nums[i] <= 5000
        All the integers of nums are unique.
        nums is sorted and rotated between 1 and n times.

        Plan:
        Binary Search
        l = 0, r = len(nums)-1, min_ele = nums[0]
        Loop while l <= r. (Check =)
            If nums[l] < nums[r], then we have a sorted subarray, so update min_ele and break the loop.
            m = (l+r) // 2
            cur_val = nums[m]
            if cur_val >= nums[r], then we know that cur_val is in the higher half of the array. So check if target
            is in the higher half of the array (so target needs to be > nums[l]) or if target > cur_val. In either
            case, set l = m, and search right. Otherwise, search left by setting r = m-1.
            Do the same thing for the opposite case.
        """
        min_ele = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                min_ele = min(min_ele, nums[l])
                break

            m = (l+r)//2
            cur_val = nums[m]
            min_ele = min(min_ele, cur_val)

            if cur_val > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min_ele


result = Solution()
print(result.findMin([3,4,5,1,2]))      # 1
print(result.findMin([4,5,6,7,0,1,2]))  # 0
print(result.findMin([11,13,15,17]))    # 11
