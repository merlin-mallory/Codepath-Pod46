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
        min_ele = nums[0]
        l, r = 0, len(nums)-1
        Loop while l <= r.
            if (nums[0] <= nums[-1]):
                Update min_ele
                Return min_ele
            m = (l + r) // 2
            cur = nums[m]
            Update min_ele
            If (cur <= nums[-1]): Search left with r = m -1. Otherwise search right with l = m + 1.
        Time: O(log(n))
        Space: O(1)
        Edge: None
        """
        min_ele = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if (nums[0] <= nums[-1]):
                min_ele = min(min_ele, nums[0])
                return min_ele
            m = (l + r) // 2
            cur = nums[m]
            min_ele = min(min_ele, cur)
            if (cur <= nums[-1]):
                r = m - 1
            else:
                l = m + 1
        return min_ele




result = Solution()
print(result.findMin([3,4,5,1,2]))      # 1
print(result.findMin([4,5,6,7,0,1,2]))  # 0
print(result.findMin([11,13,15,17]))    # 11
print(result.findMin([5,1,2,3,4]))      # 1
