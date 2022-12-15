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
        1. Hard code the mapping dict. Keys: str(digit), values: List of chars(strings).
        2. Create a substring. Loop through digits. Grab the current digit's list. Recursively explore adding each
        one to the substring, and backtracking.
        3. Base case: If length of substring == length of s, and the substring is not in added_set, then append the
        substring to the final_arr, and add the substring to the added_set.
        4. Return the final_arr
        """
        if len(digits) == 0:
            return []

        hashmap = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z']
            }
        self.final_arr = []
        self.substring = []
        self.added_set = set()

        # for i in range(len(digits)):
        self.helper(hashmap, digits, 0)

        return self.final_arr

    def helper(self, hashmap, digits, i):
        if len(self.substring) == len(digits):
            if "".join(self.substring) not in self.added_set:
                self.final_arr.append("".join(self.substring))
                self.added_set.add("".join(self.substring))
            return

        if i <= len(digits)-1:
            current_list = hashmap.get(digits[i])

            for char in current_list:
                self.substring.append(char)
                self.helper(hashmap, digits, i+1)
                self.substring.pop()
                self.added_set.discard(char)



result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))    # []
print(result.letterCombinations("2"))   # ["a","b","c"]
