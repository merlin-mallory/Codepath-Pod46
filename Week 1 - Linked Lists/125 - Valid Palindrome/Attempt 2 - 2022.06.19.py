class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
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
        1. Create a new empty string.
        2. Iterate through the input, and construct a sanitized version of the input, with only lower-case
        alphanumeric characters.
        3. Create two pointers. One pointing at the start of the string, one pointing at the end of the string,
        and move them to the middle, until they match or surpass each other. If there's a mismatch at any point,
        return false. Otherwise, return True.
        '''

        my_str = ""
        my_str_len = 0

        for i in range(len(s)):
            char = s[i]
            if char.isalnum():
                my_str += char.lower()
                my_str_len += 1

        left_pointer = 0
        right_pointer = my_str_len - 1

        while left_pointer < right_pointer:
            if my_str[left_pointer] != my_str[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True

