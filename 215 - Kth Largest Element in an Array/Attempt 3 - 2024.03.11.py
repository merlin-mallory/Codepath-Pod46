class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        215 - Kth Largest Element in an Array

        https://leetcode.com/problems/kth-largest-element-in-an-array/

        Given an integer array nums and an integer k, return the kth largest element in the array.

        Note that it is the kth largest element in the sorted order, not the kth distinct element.

        Can you solve it without sorting?

        Example 1:
        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5

        Example 2:
        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4

        Constraints:
        1 <= k <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4

        Plan:
        Minheap of size k
        Time: O(n log n)
        Space: O(n)
        Edge: None
        '''
        import heapq
        heapq.heapify(nums)
        diff = len(nums) - k
        for _ in range(diff):
            if len(nums) > k:
                heapq.heappop(nums)
        return nums[0]

