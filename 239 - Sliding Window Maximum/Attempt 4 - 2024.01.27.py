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
        1. Create deque. deque[0] will contain the max value in the window, and the rest of the values will be listed
        in descending order. We will be appending indexes to the deque, instead of values, in order to handle window
        shifting.
        2. Create final_arr.
        3. l=0, r=0.
        4. Loop while r < len(nums)
            5. Check if deque[0] < (r-k). If it is, then it is out-of-bounds, so popleft and discard, and increment l.
            6. Check if s[deque[-1]] < s[r]. If it is, then in order to maintain sort, we need to popright and discard
            5. Append r to the deque.
            6. Append deque[0] to final_arr
            7. r++
        8. return final_arr
        '''
        import collections
        deque = collections.deque()
        final_arr = []
        l, r = 0, 0
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
