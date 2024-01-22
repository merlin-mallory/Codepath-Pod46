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

        Plan: Sliding Window
        1. Initialize final_arr, window_max = 0, l = 0, r = k-1, window_dict = empty
        2. Loop k to fill up window_dict, find the first max, and append it to final_arr.
        3. Loop until r < len(nums).
            4. Remove nums[l] from the window_dict. If it was the only window_max, then find new window_max. l++
            5. r++. Add nums[r] to the window_dict. If it is greater than window_max, then update window_max.
            6. Append window_max to final_arr.
        7. Return final_arr
        Time: O(n), Space: O(1)
        '''
        import collections
        final_arr = []
        l, r = 0, 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                final_arr.append(nums[q[0]])
                l += 1

            r += 1

        return final_arr


result = Solution()

print(result.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))                  # [1]