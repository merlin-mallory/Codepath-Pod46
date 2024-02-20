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
        Backtracking
        Create stack.
        Create recurseParen(open_budget, closed_budget).
        Call recurseParen(n, n)
        Return final_arr

        Time: O(2^n)
        Space: O(n)
        Edge: None)
        '''
        stack = []
        final_arr = []
        def recurseParen(open_budget, closed_budget):
            # Base case
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return

            # Recursive Case 1
            if open_budget > 0:
                stack.append("(")
                recurseParen(open_budget-1, closed_budget)
                stack.pop()

            if closed_budget > 0 and closed_budget > open_budget:
                stack.append(")")
                recurseParen(open_budget, closed_budget-1)
                stack.pop()

        recurseParen(n,n)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]