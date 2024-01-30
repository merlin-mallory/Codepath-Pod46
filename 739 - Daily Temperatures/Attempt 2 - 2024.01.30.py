from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that
        answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is
        no future day for which this is possible, keep answer[i] == 0 instead.

        Example 1:
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]

        Example 2:
        Input: temperatures = [30,40,50,60]
        Output: [1,1,1,0]

        Example 3:
        Input: temperatures = [30,60,90]
        Output: [1,1,0]

        Constraints:
        1 <= temperatures.length <= 10^5
        30 <= temperatures[i] <= 100

        Plan:
        Stack
        1. Init answer = [0] * len(temperatures). Init pairs = [], which will contain (value, index) tuples
        2. Loop through pairs.
            3. If temperatures[i][0] < stack[-1], then we found a value. answer[i] = i - index.
        '''
        final_arr = [0] * len(temperatures)
        stack = []

        for right_i, right_val in enumerate(temperatures):
            while stack and right_val > stack[-1][0]:
                left_val, left_i = stack.pop()
                final_arr[left_i] = (right_i - left_i)
            stack.append([right_val, right_i])
        return final_arr

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
