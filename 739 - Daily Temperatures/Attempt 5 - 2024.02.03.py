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
        1. Init answer = [0] * len of temperatures
        2. Loop through temperatures.
            3. If there is a stack and temperatures[r] > stack[-1], then pop the stack, and calculate that pair's
            days_to_wait.
            4. Append [temperatures[i], i] to the stack.
        5. Return answer.
        '''
        stack = []
        answer = [0] * len(temperatures)
        for r in range(len(temperatures)):
            while stack and temperatures[r] > stack[-1][0]:
                val, l = stack.pop()
                answer[l] = r - l
            stack.append([temperatures[r], r])
        return answer

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
