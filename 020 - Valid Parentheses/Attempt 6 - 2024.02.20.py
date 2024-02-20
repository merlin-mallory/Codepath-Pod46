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
        Create closed_to_open dict.
        Loop through s.
            if char not in closed_to_open:
                Append char to stack
            else
                Check if stack[-1] has an open bracket type matching char. If so, pop the top of the stack.
                Otherwise, return False.
        If we finish the loop and the stack is empty, then return True, otherwise return False.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        closed_to_open = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for char in s:
            if char not in closed_to_open:
                # Open bracket found
                stack.append(char)
            else:
                # Closed bracket found
                if stack and stack[-1] == closed_to_open[char]:
                    stack.pop()
                else:
                    return False
        return not stack


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
