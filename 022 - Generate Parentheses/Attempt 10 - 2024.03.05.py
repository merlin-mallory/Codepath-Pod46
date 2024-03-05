from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        Example 2:
        Input: n = 1
        Output: ["()"]

        Constraints:
        1 <= n <= 8

        Plan:
        Stack Backtracking
        Create stack = []
        Create final_arr = []
        Create backtrack(open_budget, closed_budget) function.
            Base Case 1: If open_budget == closed_budget == 0, then join the stack, append to final_arr, and return.
            Recursive Case 1: If open_budget > 0, then append "(" to the stack, and backtrack(open_budget - 1,
            closed_budget). Upon return, pop from the stack.
            Recursive Case 2: If closed_budget > 0 and (closed_budget > open_budget), then append "(" to the stack,
            and backtrack(open_budget, closed_budget). Upon return, pop from the stack.
            Return
        Call backtrack(n, n).
        Return final_arr
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        final_arr = []
        def backtrack(open_budget, closed_budget):
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return
            if open_budget > 0:
                stack.append("(")
                backtrack(open_budget - 1, closed_budget)
                stack.pop()
            if (closed_budget > 0) and (closed_budget > open_budget):
                stack.append(")")
                backtrack(open_budget, closed_budget - 1)
                stack.pop()
            return
        backtrack(n, n)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]