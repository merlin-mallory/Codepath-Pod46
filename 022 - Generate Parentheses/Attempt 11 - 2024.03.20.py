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
        Create stack, final_arr.
        Create recurse(open_budget, closed_budget) function. Modifies the stack and eventually appends the stack to
        the final_arr.
            Base Case: If open_budget == closed_budget == 0, then join the stack and append to the final_arr,
            and return.
            Recursive Case 1: If open_budget > 0, then append "(" to stack, and recurse(open_budget - 1,
            closed_budget). Pop from stack on return.
            Recursive Case 2: If closed_budget > 0 and (open_budget < closed_budget), then append ")" to stack,
            and recurse (open_budget, closed_budget - 1). Pop from stack on return.
        Call recurse(n, n)
        Return final_arr.
        Time: O(2^n)
        Space: O(1)
        Edge: None
        '''
        stack = []
        final_arr = []
        def dfs(open_budget, closed_budget):
            if open_budget == closed_budget == 0:
                final_arr.append(''.join(stack))
                return
            if open_budget > 0:
                stack.append("(")
                dfs(open_budget-1, closed_budget)
                stack.pop()
            if closed_budget > 0 and (open_budget < closed_budget):
                stack.append(")")
                dfs(open_budget, closed_budget - 1)
                stack.pop()
        dfs(n, n)
        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]