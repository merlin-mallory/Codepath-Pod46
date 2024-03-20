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
        Create closed_to_open dict manually.
        Create stack.
        Loop through s.
            Check if cur is not in closed_to_open. If that's the case, then append cur to the stack.
            Otherwise, check if cur == closed_to_open[stack[-1]]. If that's the case, then pop the stack. Otherwise
            return False.
        Return True if the stack is empty, otherwise return False.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        closed_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for c in s:
            if c not in closed_to_open:
                stack.append(c)
            else:
                if stack and (stack[-1] == closed_to_open[c]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
