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
        1. stack = [], current_val = tokens[0]
        2. Loop through tokens.
            3. If the token is a number, then append it to the stack.
            4. Otherwise, pop 2 values from the stack, and use the desired operator. Append that result to stack.
        5. Return stack[0]
        Edge Cases: Always truncating toward zero means we need negative floats to go up, and floats to go up.
        Time: O(n), Space: O(n)
        '''
        stack = []

        for token in tokens:
            if token == "+":
                right_val, left_val = stack.pop(), stack.pop()
                result_val = left_val + right_val
            elif token == "-":
                right_val, left_val = stack.pop(), stack.pop()
                result_val = left_val - right_val
            elif token == "*":
                right_val, left_val = stack.pop(), stack.pop()
                result_val = left_val * right_val
            elif token == "/":
                right_val, left_val = stack.pop(), stack.pop()
                result_val = left_val / right_val
                result_val = int(result_val)
            else:
                result_val = int(token)

            stack.append(result_val)

        return stack[0]

result = Solution()
print(result.evalRPN(["2", "1", "+", "3", "*"]))  # 9
print(result.evalRPN(["4", "13", "5", "/", "+"]))  # 6
print(result.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
