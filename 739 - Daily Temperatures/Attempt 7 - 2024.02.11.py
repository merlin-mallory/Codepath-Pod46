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
        Init stack, answer.
        Loop through temperatures.
            Compare temperatures[i] < stack[-1][0] ? stack.pop(), calc wait_time, update answer
            Append [temperatures[i], i] to the stack.
        Return answer
        Time: O(n)
        Space: O(n)
        Edge: Possiblity of len 1 temperatures.
        '''
        stack = []
        answer = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            while stack and (temperatures[i] > stack[-1][0]):
                stack_v, stack_i = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append([temperatures[i], i])
            i += 1
        return answer

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
