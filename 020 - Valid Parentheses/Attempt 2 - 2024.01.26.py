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
        1. Create closed_to_open dict. Keys: Closing brackets, Values: Matching opening brackets.
        2. Create stack.
        3. Loop through s.
            4. Check if s[i] is in closed_to_open. If it is, then it is a closing bracket, so check the top of the
            stack to see if the top of the stack = closed_to_open[s[i]]. If there's a match, then we can pop the top
            of the stack and keep going. If its a mismatch, the return False. Also, if the stack is empty,
            return false, because we can't begin with a starting bracket.
            5.Otherwise, we've found an opening bracket, which we can append to the stack.
        6. If our stack is empty after the loop completes, then we can return True. Otherwise, if there's still junk
        in the stack, then there's a mismatch, so return False.
        Time: O(n), Space: O(n)
        Edge Case: len(s) == 1?
        '''
        if len(s) == 1:
            return False

        import collections
        closed_to_open = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []

        for i in range(len(s)):
            if s[i] in closed_to_open:
                # We found a closing bracket
                if stack and (stack[-1] == closed_to_open[s[i]]):
                    stack.pop()
                else:
                    return False
            else:
                # We found an opening bracket
                stack.append(s[i])

        if not stack:
            return True
        else:
            return False


result = Solution()
print(result.isValid("()"))     # True
print(result.isValid("()[]{}")) # True
print(result.isValid("(]"))     # False
print(result.isValid("([)]"))   # False
