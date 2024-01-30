from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        150 - Evaluate Reverse Polish Notation

        https://leetcode.com/problems/evaluate-reverse-polish-notation/

        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

        Note that:

        The valid operators are '+', '-', '*', and '/'.
        Each operand may be an integer or another expression.
        The division between two integers always truncates toward zero.
        There will not be any division by zero.
        The input represents a valid arithmetic expression in a reverse polish notation.
        The answer and all the intermediate calculations can be represented in a 32-bit integer.

        Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

        Example 3:
        Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        Output: 22
        Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22

        Constraints:

        1 <= tokens.length <= 10^4
        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

        Plan:
        Stack
        1. Init stack = []
        2. Loop through tokens.
            3. If its a int, then append it to the stack.
            4. Otherwise, pop twice from the stack. The first pop will be the right value, the second pop will be the
            second value. If the token is "+", then result = left+right. If the token is "-", then result = left -
            right. If the token is "*", then result = left*right. If the token is "/", then result = left / right,
            and then int-ify in order to round towards zero. Regardless of the token, append the result to the stack.
        5. After the loop finishes, there should be only one value remaining in the stack, which will be the final
        result. Return it.
        '''
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                right_val, left_val = stack.pop(), stack.pop()
                if token == "+":
                    result = left_val + right_val
                elif token == "-":
                    result = left_val - right_val
                elif token == "*":
                    result = left_val * right_val
                else:   # token == "/"
                    result = left_val / right_val
                    result = int(result)
                stack.append(result)
        return stack[0]


result = Solution()
print(result.evalRPN(["2","1","+","3","*"]))                                        # 9
print(result.evalRPN(["4","13","5","/","+"]))                                       # 6
print(result.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))    # 22
