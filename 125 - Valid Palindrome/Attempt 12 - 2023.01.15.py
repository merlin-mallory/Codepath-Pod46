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

        1 <= s.length <= 2 * 10^5
        s consists only of printable ASCII characters.

        Plan:
        1. Sanitize the input, transform to array
        2. Implement two pointers solution, returning false if there's ever a mismatch. And returning true if left_i
        = right_i.
        '''

        # Sanitize input
        new_arr = []
        for char in s:
            if char.isalnum():
                new_arr.append(char.lower())

        # Implement two pointers
        left, right = 0, len(new_arr)-1
        while left < right:
            if new_arr[left] != new_arr[right]:
                return False
            left += 1
            right -= 1
        return True


