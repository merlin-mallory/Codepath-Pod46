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
        1. Hard-code a mapping_dict. Keys: Digits from 2 to 9 as strings, Values: List containing the 3-4 possible
        characters for that digit.
        2. Create a subarray and final_arr.
        3. Loop through each index in digits. Grab the list_of_possible_chars from the mapping dictionary. Loop
        through the list, appending the character to the subarray, and  recursively calling a helper function with i++.
        When the length of the subarray equals the length of digits, then join and append the subarray to the final_arr.
        4. Return the final array.
        """
        if len(digits) == 0:
            return []

        mapping_dict = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
            }

        subarray = []
        final_arr = []

        def helper(subarray, i):
            if len(subarray) == len(digits):
                final_arr.append("".join(subarray))
                return

            current_digit = digits[i]
            current_list = mapping_dict.get(current_digit)
            for char in current_list:
                subarray.append(char)
                helper(subarray, i+1)
                subarray.pop()

        helper(subarray, 0)

        return final_arr


result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))    # []
print(result.letterCombinations("2"))   # ["a","b","c"]