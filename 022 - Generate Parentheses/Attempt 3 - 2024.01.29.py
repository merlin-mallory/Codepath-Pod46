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
        Stack, Recursion
        1. Global vars: stack, final_arr, open_budget, closed_budget.
        2. RecurseParen function
        3. Call RecurseParen function.
            4. Base Case: open_budget == closed_budget == 0, join and append the stack to the final_arr, and return.
            5. Recursive Case 1: If open_budget > 0, then add a "(" to the stack, recurse with open_budget-1,
            and pop stack upon return.
            6. Recurse Case 2: If closed_budget > 0 and closed_budget > open_budget, then add a ")" to the stack,
            recurse with closed_budget-1, and pop stack upon return
        4. Return final_arr
        Time: O(n^2), Space: O(n)
        Edge Cases: None
        '''
        stack = []
        final_arr = []

        def recurseParent(open_budget, closed_budget):
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return

            if open_budget > 0:
                stack.append('(')
                recurseParent(open_budget-1, closed_budget)
                stack.pop()

            if closed_budget > 0 and (closed_budget > open_budget):
                stack.append(')')
                recurseParent(open_budget, closed_budget-1)
                stack.pop()

        recurseParent(n, n)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]