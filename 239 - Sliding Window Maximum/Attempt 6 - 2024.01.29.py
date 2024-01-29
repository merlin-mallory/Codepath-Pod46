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
        1. Create decreasing order deque (name)? The deque will store the window's current max value in index 0,
        and all of the other values in the deque will be stored in decreasing order. However we will add indexes to
        the deque instead of the values themselves, in order to determine when a value is outside of the current window.
        2. Init final_arr = [], l = 0, r = 0
        3. Loop while r < len(nums).
            4. Check if deque[0] < l. If it is, then its outside the window, so popleft() and discard.
            5. Check if nums[deque[-1]] < nums[r]. If it is, then in order to maintain decreasing order, we need to
            pop and discard.
            6. Append r to the deque.
            7. Check if r-l+1 == k
                8. Append nums[0] to the final arr
                9. l += 1
            10. r++
        Time: O(n)
        Space: O(n)
        Edge Cases: None
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
            if (r-l+1) == k:
                final_arr.append(nums[deque[0]])
                l += 1
            r += 1

        return final_arr


result = Solution()

print(result.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))  # [1]
