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
        stack = []
        closed_to_open = { ')':'(', ']':'[', '}':'{' }
        Loop cur through s.
            if cur in closed_to_open:
                if stack[-1] == closed_to_open[cur]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur)
        return True if not stack else False
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        closed_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for cur in s:
            if cur in closed_to_open:
                if stack and stack[-1] == closed_to_open[cur]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(cur)

        return True if not stack else False


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
