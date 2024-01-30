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
        1. Init stack = []
        2. Loop through s.
            3. If s[i] == open bracket, then add it to the stack.
            4. Otherwise, check if s[i]'s bracket type matches stack[-1]. If it does, then pop the stack and
            continue. Otherwise, return false. If there's no stack, then return False, because we can't start with a
            closed bracket.
        5. If we finish the loop and there's something still in the stack, then return False, Otherwise return true.
        '''
        stack = []
        closed_to_open = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in range(len(s)):
            cur_char = s[i]
            if cur_char in closed_to_open:
                if stack and stack[-1] == closed_to_open[cur_char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur_char)

        return not stack


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
