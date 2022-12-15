class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
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
        1. Sanitize the input. Loop through s, and create new_s.
        2. Check for palindrome status. Left = index 0, right = index len(new_s)-1. If new_s[left] != new_s[right],
        then return False. Otherwise, left++ and right --. The loop should complete when right < left. If the loop
        completed, then we've verified a palindrome, so return true.
        """

        new_s = ""

        # Sanitizing input to include only alphanumeric characters
        for i in range(len(s)):
            if s[i].isalnum():
                new_s = new_s + s[i].lower()

        # Checking for palindrome...
        left = 0
        right = len(new_s)-1
        while right > left:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        # Check complete, we have verified a palindrome

        return True
