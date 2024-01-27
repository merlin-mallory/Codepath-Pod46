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
        '''

result = Solution()
print(result.generateParenthesis(3))    # ["((()))","(()())","(())()","()(())","()()()"]
print(result.generateParenthesis(1))    # ["()"]