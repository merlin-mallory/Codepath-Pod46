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
        1. Sanitize the input by lower-casing the data, and stripping out the non-alphanumeric characters.
        2. Use the two pointer technique to loop through the array and verify that the santized_s is a palindrome. If
        there's a mismatch at any point, then return False. Otherwise, if we eventually reach left_pointer =
        right_pointer, then we've verified that the resultant string is a palindrome, so return True.
        '''

        # I was on the right track, but my first mistake was setting the right pointer to len(sanitized_s),
        # instead of len(sanitized_s)-1. Second mistake was forgetting to lowercase the santized input. But it looks
        # like it was fine to leave the

        sanitized_s = []
        for i in range(len(s)):
            if s[i].isalnum():
                sanitized_s.append(s[i].lower())
        print("final sanitized s:", sanitized_s)

        left_pointer, right_pointer = 0, len(sanitized_s)-1
        while left_pointer < right_pointer:
            if sanitized_s[left_pointer] != sanitized_s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True
