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
        Create stack.
        Create closed_to_open dict. Manually init.
        Loop through s.
            If s[i] in closed_to_open, then check if closed_to_open[s[i]] = stack[-1]. If so, pop the stack,
            otherwise return False.
            If s[i] is not in closed_to_open, then append it to the stack.
        return len(stack) == 0
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        closed_to_open = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for char in s:
            if char in closed_to_open:
                if stack and closed_to_open[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
