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
        Clean the input
        Compare the cleaned_str with the reversed str. Return True if there's a match, otherwise False.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        cleaned_arr = []
        for char in s:
            if char.isalnum():
                cleaned_arr.append(char.lower())
        return cleaned_arr == cleaned_arr[::-1]
