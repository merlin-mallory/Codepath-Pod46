class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        https://leetcode.com/problems/search-insert-position/description/

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Input: nums = [1,3,5,6], target = 7
        Output: 4

        Constraints:

        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums contains distinct values sorted in ascending order.
        -10^4 <= target <= 10^4

        Plan:
        1. Looks like binary search.
        2. Left = 0, right = len(nums)-1.
        3. The tricky part is going to be figuring out which index to return if the target is not found. I'll have to
        test for that.
        '''

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:  # nums[mid] == target
                return mid

        return left
