class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        https://leetcode.com/problems/valid-palindrome/

        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
        non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
        and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.

        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.

        Constraints:

        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.

        Plan:
        1. Sanitize the input. Loop through the string, and construct a new_str that contains only lower case
        characters.
        2. left_pointer = 0, right_pointer = len(new_str)-1
        3. While right_pointer > left_pointer:
            4. If new_str[left_pointer] != new_str[right_pointer]:
                5. Return False
            6. left_pointer += 1, right_pointer -=1
        7. If we finish the loop without returning False, then the pointers have reached the middle of the string,
        and we've confirmed that the string is a Palindrome.
        '''

        new_str = ''

        for char in s:
            if char.isalnum():
                new_str = new_str + char.lower()

        left_pointer, right_pointer = 0, len(new_str)-1

        while right_pointer > left_pointer:
            if new_str[left_pointer] != new_str[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True
