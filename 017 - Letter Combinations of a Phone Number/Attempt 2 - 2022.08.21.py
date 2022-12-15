from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
        could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map
        to any letters.

        Constraints:
        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].

        Plan:
        1. Looks like a backtracking solution.
        2. Create a mapping_dict. Keys = digits, values = list of chars that correspond with the digit.
        3. Loop through digits. Grab the list of chars corresponding to that digit. Loop through the list,
        and explore adding the char, and then recursively create all possible substrings, eventually appending a
        substring that reaches len(digits). Then backtrack and pop off the inital pick from the mapping_dict.
        4. After we explore the entire tree, return the final_arr.
        """
        if len(digits) == 0:
            return []

        final_arr = []
        mapping_dict = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
            }

        final_arr = []
        substring = []
        i = 0

        def helper(substring, i):
            if len(substring) == len(digits):
                final_arr.append("".join(substring))
                return

            current_digit = int(digits[i])
            current_list = mapping_dict.get(current_digit)
            for char in current_list:
                substring.append(char)
                helper(substring, i+1)
                substring.pop()

        helper(substring, i)

        return final_arr



result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))    # []
print(result.letterCombinations("2"))   # ["a","b","c"]