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
        1. Initialize stack.
        2. Loop through tokens.
            3. Check if token is a number. If so, then int it, and append it to the stack.
            4. Otherwise, we know that token is an operator. So we need to handle each one individually.
                5. Pop twice from the stack. The first one will be the right_val, the second one will be the left_val.
                6. Addition: left_val + right_val
                7. Subtraction: left_val - right_val
                8. Multiplication: left_val * right_val
                9. Division: left_val / right_val. And then use int() to truncate towards 0.
        10. After the loop finishes, the final value should be the only value in the stack, so return stack[0].
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
                else:   #token = "/"
                    result = left_val / right_val
                    result = int(result)

                stack.append(result)

        return stack[0]


result = Solution()
print(result.evalRPN(["2","1","+","3","*"]))                                        # 9
print(result.evalRPN(["4","13","5","/","+"]))                                       # 6
print(result.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))    # 22
