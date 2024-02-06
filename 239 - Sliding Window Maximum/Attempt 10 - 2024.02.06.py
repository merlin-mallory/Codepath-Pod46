from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        239. Sliding Window Maximum

        https://leetcode.com/problems/sliding-window-maximum/

        You are given an array of integers nums, there is a sliding window of size k which is moving from the very
        left of the array to the very right. You can only see the k numbers in the window. Each time the sliding
        window moves right by one position.

        Return the max sliding window.

        Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length

        Plan:
        Sliding Window
        Init a monotonic decreasing order deque. It will contain the maximum value of the window at deque[0],
        and the other values of the deque will be stored in decreasing order. However we will append indexes
        referencing values to the deque instead of the values themselves, in order to more easily check for when
        values inside of the deque go out-of-bounds.
        Init final_arr = []
        l = 0, r = 0
        Loop while r < len(nums).
            Clean the left side of the deque. If deque[0] < l, then popleft and discard.
            Clean the right side of the deque. If nums[deque[-1]] < nums[r], then popright and discard.
            Append r to the deque.
            If r+1 >= k:
                Append nums[deque[0]] to final_arr.
                l--
        Return final_arr
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        import collections
        deque = collections.deque()
        final_arr = []
        l, r = 0, 0
        while r < len(nums):
            while deque and deque[0] < l:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)
            if r+1 >= k:
                final_arr.append(nums[deque[0]])
                l += 1
            r += 1
        return final_arr


result = Solution()

print(result.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))                  # [1]
