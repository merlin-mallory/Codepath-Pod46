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
        1. Init final_arr = [], stack = []
        2. Create recurseParen(open_budget, closed_budget) function.
            3. Base Case: open_budget == closed_budget == 0, join and append the stack to the final arr, and return.
            4. Recursive Case 1: If open_budget > 0, then append "(" to the stack, recurse open_budget-1,
            and upon return, pop from stack.
            5. Recursive Case 2: If closed_budget > 0 and open_budget < closed_budget, then append ")" to the stack,
            recurse closed_budget-1, and upon return, pop from stack.
        3. Call recurseParen(n,n)
        4. Return final_arr.
        Time: O(2^n)
        Space: O(n)
        Edge: None
        '''
        final_arr = []
        stack = []
        def recurseParen(open_budget, closed_budget):
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return

            if open_budget > 0:
                stack.append('(')
                recurseParen(open_budget - 1, closed_budget)
                stack.pop()

            if closed_budget > 0 and open_budget < closed_budget:
                stack.append(')')
                recurseParen(open_budget, closed_budget - 1)
                stack.pop()

        recurseParen(n, n)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]