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
        1. Create pairs array, which will contain [temp, ind] pairs. Init answer = [].
        2. Loop through pairs.
            3. If there's stack and pairs[r][0] > stack[-1][0], then pop from the stack, and fill in that index in
            the answer array. Calculate the wait by r - popped ind, and then set answer[popped_ind] to that value.
            4. Append pairs[r] to the stack.
        5. Return answer.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        answer = [0] * len(temperatures)

        for r_ind in range(len(temperatures)):
            while stack and temperatures[r_ind] > stack[-1][0]:
                l_val, l_ind = stack.pop()
                answer[l_ind] = r_ind - l_ind
            stack.append([temperatures[r_ind], r_ind])

        return answer

result = Solution()
print(result.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(result.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
print(result.dailyTemperatures([30,60,90]))                 # [1,1,0]
