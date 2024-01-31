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
        1. Init stack = [] (value, index pairs), answer = [0] * len(temperatures). l = 0, r = 0.
        2. Loop while r < len(temperatures)
            4. If there is a stack, and s[r] > stack[-1][0], then pop from the stack, calculate the len r - i,
            update that index in answer.
            3. Append s[r] to the stack.
        9. Return answer
        '''
        stack = []
        answer = [0] * len(temperatures)
        for right_i in range(len(temperatures)):
            while stack and temperatures[right_i] > stack[-1][0]:
                left_val, left_i = stack.pop()
                current_len = right_i - left_i
                answer[left_i] = current_len
            stack.append([temperatures[right_i], right_i])
        return answer

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
