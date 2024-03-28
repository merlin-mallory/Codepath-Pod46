from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
        could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map
        to any letters.

        {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }

        Constraints:
        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].

        Plan:
        Backtracking
        Time: O(4^n), where n = length of digits
        Space: O(h)
        Edge: Could be 0 len digits
        """
        if not digits: return []

        digits_to_chars = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }

        final_arr = []
        stack = []
        def backtrack(i):
            if len(stack) == len(digits):
                final_arr.append("".join(stack))
                return
            # if i >= len(digits): return
            cur_digit = digits[i]
            list_of_chars = digits_to_chars[cur_digit]
            for c in list_of_chars:
                stack.append(c)
                backtrack(i+1)
                stack.pop()
            return
        backtrack(0)
        return final_arr

result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))    # []
print(result.letterCombinations("2"))   # ["a","b","c"]