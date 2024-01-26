class Solution:
    def isValid(self, s: str) -> bool:
        '''
        020 - Valid Parentheses

        https://leetcode.com/problems/valid-parentheses/

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string
        is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Example 1:

        Input: s = "()"
        Output: true
        Example 2:

        Input: s = "()[]{}"
        Output: true
        Example 3:

        Input: s = "(]"
        Output: false

        Constraints:

        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.

        Plan:
        Stack
        1. stack = [], curled = 0, square = 0, curl = 0
        2. Loop through s, and append s[i] to the stack. open brakets increase type +1, closed brackets decrease type -1
        3. If all 3 != 0, then return False.
        4. Pop the stack, making sure that every open is matched with a close.
        '''
        stack = []
        closed_to_open_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in closed_to_open_dict:
                if stack and stack[-1] == closed_to_open_dict[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


result = Solution()
print(result.isValid("()"))  # True
print(result.isValid("()[]{}"))  # True
print(result.isValid("(]"))  # False
print(result.isValid("([)]"))  # False
