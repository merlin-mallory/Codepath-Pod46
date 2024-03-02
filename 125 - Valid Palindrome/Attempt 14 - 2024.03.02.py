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
        Array
        1. Sanitize the string by stripping all non alphanumeric characters
        2. Return s == s[::-1]
        Time: O(n)
        Space: O(1)
        '''
        arr1 = []
        for char in s:
            if char.isalnum():
                arr1.append(char.lower())
        l, r = 0, len(arr1)-1
        while l <= r:
            if arr1[l] != arr1[r]: return False
            l += 1
            r -= 1
        return True

