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
        Stack Recursion
        Create stack and final_arr.
        Create recurseParen function(open_budget, closed_budget).
            Base case: If open_budget == closed_budget == 0, join the stack and append it to the final_arr,
            and then return.
            Recursive case 1: If openbudget > 0, then recurse with (open_budget-1, closed_budget), and upon return
            pop from the stack.
            Recursive case 2: If closed_budget > 0 and open_budget < closed_budget, then recurse with (open_budget,
            closed_budget - 1), and upon return pop from the stack.
        Call recurseParen function(n, n)
        Return final_arr
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        final_arr = []

        def recurseParen(open_budget, closed_budget):
            # Base Case
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return
            if open_budget > 0:
                stack.append("(")
                recurseParen(open_budget - 1, closed_budget)
                stack.pop()
            if (closed_budget > 0) and (open_budget < closed_budget):
                stack.append(")")
                recurseParen(open_budget, closed_budget-1)
                stack.pop()

        recurseParen(n, n)
        return final_arr



result = Solution()
print(result.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))  # ["()"]




