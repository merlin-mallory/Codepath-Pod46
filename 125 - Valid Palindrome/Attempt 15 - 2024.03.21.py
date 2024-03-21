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
        Two Pointers
        Create final_arr.
        Loop through s.
            if c.isAlpha(), append c.lower() to final_arr.
        l, r = 0, len(final_arr)-1
            if final_arr[l] != final_arr[r], return False
            l++
            r--
        Return True
        Time: O(n)
        Space: O(1) or O(n) depending upon classification of output space.
        Edge: None
        '''
        final_arr = []
        for c in s:
            if c.isalnum():
                final_arr.append(c.lower())
        l, r = 0, len(final_arr)-1
        while l <= r:
            if final_arr[l] != final_arr[r]: return False
            l += 1
            r -= 1
        return True
