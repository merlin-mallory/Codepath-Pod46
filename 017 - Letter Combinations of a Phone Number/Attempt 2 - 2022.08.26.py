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
        1. Hard code the map from digits to characters. Keys = digits from 2 to 9, Values = list of char strings.
        2. Create a substring. Loop through digits, pull the appropriate list from the hashmap, explore adding each
        possible char to the substring. When the length of the substring equals the length of digits, append that
        substring to the final array, and backtrack.
        3. After exploring the entire recursive tree, return the result.
        4. Time complexity is going to be 2^n, where n is the length of digits. Each step of the recursive tree
        involves a single choice (either we add the char or don't, and there is a maximum of 4n chars per digit),
        and the height of the recursive tree will be the length of digits. Space complexity is going to be 2^n (
        maybe?)
        """
        if not digits:
            return []

        digits_to_chars = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
            }

        substring = []
        final_arr = []

        def backtrack_helper(substring, i):
            if len(substring) == len(digits):
                final_arr.append("".join(substring))
                return

            current_digit = digits[i]
            current_list = digits_to_chars.get(current_digit)
            for possibility in current_list:
                substring.append(possibility)
                backtrack_helper(substring, i+1)
                substring.pop()
            return

        backtrack_helper(substring, 0)

        return final_arr

result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))    # []
print(result.letterCombinations("2"))   # ["a","b","c"]
