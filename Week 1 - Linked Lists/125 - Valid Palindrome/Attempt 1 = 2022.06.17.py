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
        1. Sanitize the data. Remove all non-alpha characters, and make alpha chars lowercase.
        2. Use the two pointer technique to compare characters at each of the string. While the
           characters match, move the pointers to the middle of the string. If the characters
           do not match at any time, return False. Otherwise, when the pointers pass each other,
           break the loop, and return True.
        3. Time: Sanitizing data is O(n). Two pointer technique is O(n). Overall: O(n)
           Space: We need to create a new string, so O(n).
        '''

        new_str = ""

        for i in range(len(s)):
            this_char = s[i]
            if this_char.isalnum():
                new_str += s[i].lower()

        left_pointer = 0
        right_pointer = len(new_str) - 1

        while right_pointer >= left_pointer:
            if new_str[right_pointer] != new_str[left_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True


my_str = "race a car"
result = Solution()
final_result = result.isPalindrome(my_str)
print(final_result)

# Optimal result:

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         i, j = 0, len(s) - 1
#
#         while i < j:
#             while i < j and not s[i].isalnum():
#                 i += 1
#             while i < j and not s[j].isalnum():
#                 j -= 1
#
#             if s[i].lower() != s[j].lower():
#                 return False
#
#             i += 1
#             j -= 1
#
#         return True