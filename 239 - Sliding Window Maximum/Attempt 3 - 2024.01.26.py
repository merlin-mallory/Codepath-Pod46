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
        1. Create a deque. Index 0 will hold the max value in the window, and the rest of the values will be held in
        decreasing order.
        2. l = 0, r = 0, final_arr = []
        3. Loop while r < len(nums)
            4. Check deque[0] to see if its < (r - k). If it is, then it is out-of-bounds, so popleft and discard
            5. Check deque[-1] to see if its < s[r]. If it is, then that value doesn't matter anymore for the window,
            so popright and discard.
            6. Append r to the deque
            7. Append nums[deque[0]] to final_arr
            8. r += 1
        9. return final_arr
        Time: O(n), Space: O(n)
        Edge Cases: None
        '''
        import collections
        deque = collections.deque()
        l, r = 0, 0
        final_arr = []
        while r < len(nums):
            if deque and l > deque[0]:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)
            if (r+1) >= k:
                final_arr.append(nums[deque[0]])
                l += 1
            r += 1
        return final_arr


result = Solution()

print(result.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))                  # [1]
print(result.maxSlidingWindow([1, -1], 1))              # [1, -1]
