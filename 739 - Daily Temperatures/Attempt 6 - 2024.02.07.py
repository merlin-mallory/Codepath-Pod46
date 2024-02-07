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
        Loop through temperatures, construct [temperatures[i], i] pairs, and append to the stack. Compare the
        cur_temp with stack[-1][0]. If the cur_temp is greater, then we found a higher temp for the day on top of the
        stack, so pop the stack, and compare the cur_temp[i] with the stack[-1][1] value, and fill in answer[i].
        We should init the answer array with zeros in order to handle the possibility of there not being a warmer day.
        Return answer.
        '''
        answer = [0] * len(temperatures)
        stack = []
        for cur_i, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][0]:
                stack_val, stack_i = stack.pop()
                answer[stack_i] = cur_i - stack_i
            stack.append([cur_temp, cur_i])
        return answer

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
