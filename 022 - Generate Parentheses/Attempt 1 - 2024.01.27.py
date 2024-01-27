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
        Stack
        1. We want to return a len(n) * 2 string and append it to final_arr.
        2. There should always be more or equal number of opening parenthesis in the stack.
        3. Maybe do a recursion, keeping track of number of opened and closed parentheses.
        '''
        stack = []
        final_arr = []
        def recurse_paren(opened_count, closed_count):
            if opened_count == closed_count == n:
                final_arr.append("".join(stack))
                return

            if opened_count < n:
                stack.append("(")
                recurse_paren(opened_count + 1, closed_count)
                stack.pop()

            if closed_count < opened_count:
                stack.append(")")
                recurse_paren(opened_count, closed_count + 1)
                stack.pop()

        recurse_paren(0, 0)

        return final_arr

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]