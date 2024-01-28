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
        Stack/Recursion

        1. Base case: When open_budget == closed_budget == 0, append to final_arr.
        2. Recursive case 1: If we have open_budget, then add a open paraen, and recurse, and post-recurse, pop.
        3. Recursive case 2: If we have closed_budget, and open_budget <= closed_budget, then add a closed paren,
        and recurse, and post-recurse, pop.
        '''
        final_arr = []
        stack = []
        open_budget, closed_budget = n, n

        def recurseParen(open_budget, closed_budget):
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return

            if open_budget > 0:
                stack.append("(")
                recurseParen(open_budget - 1, closed_budget)
                stack.pop()

            if closed_budget > 0 and closed_budget > open_budget:
                stack.append(")")
                recurseParen(open_budget, closed_budget - 1)
                stack.pop()

        recurseParen(open_budget, closed_budget)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]