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
        1. Create final_arr.
        2. Outer loop through temperatures.
            3. Inner loop i+1
                4. counter = 0
                5. If temperatures[j] <= temperatures[i], then counter++ and j++.
                6. Otherwise,  final_arr.append(counter), and j++
        7. Return final_arr
        Edge Case: None
        Time: O(n^2)
        Space: O(1) (if final_arr doesn't count)
        '''
        final_arr = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                final_arr[stackInd] = (i - stackInd)
            stack.append([t, i])
        return final_arr

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
