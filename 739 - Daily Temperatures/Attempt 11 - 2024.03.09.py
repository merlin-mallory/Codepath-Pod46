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
        Create stack, and answer (init to 0).
        Loop through temperatures.
            If there's a stack, compare temp[i] with stack[-1][1]. If >, then pop the stack, calc wait, and insert
            into answer[stack_i].
            Append [i, temp[i]] to the stack
        Return answer.
        '''
        stack = []
        answer = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and (val > stack[-1][1]):
                stack_i, _ = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append([i, val])
        return answer


result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
