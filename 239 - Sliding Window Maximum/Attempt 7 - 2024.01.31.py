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
        Sliding Window with Deque
        1. Create monotonic decreasing order deque. This will hold the window's current maximum in the zero-index,
        and the remainder of the values will be stored in decreasing order. However, we will store indexs in the
        deque instead of values, in order to more easily decide when to discard values.
        2. Init final_arr = [], l = 0, r = 0.
        3. Loop while r < len(nums).
            3. Check if deque[0] < l, then we should popleft and discard.
            4. Check if nums[deque[-1]] < nums[r], then we should pop and discard
            5. Append r to deque.
            6. If r+1 >= k, then we should update the final_arr, and adjust l.
                6. Append deque[0] to the final_arr.
                7. l++
            7. r++
        10. Return final_arr.
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
            if r+1 >= k:
                final_arr.append(nums[deque[0]])
                l += 1
            r += 1
        return final_arr


result = Solution()

print(result.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))                  # [1]
