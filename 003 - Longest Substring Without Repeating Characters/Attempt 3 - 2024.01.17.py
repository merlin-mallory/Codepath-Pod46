class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Given a string s, find the length of the longest substring without repeating characters.

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.

        Plan:
        Sliding Window
        1. Initialize pointers. l = 0, r = 1, current_len = 0, longest_substring_len = 0, current_set = set()
        2. Loop until the right pointer reaches the end of the list. Check if the current char is in the current set.
           If it is, then set current_len = 0, and remove the char at the left pointer from the current set,
           and iterate the left pointer. Otherwise, iterate current_len, update the max longest_substring_len,
           and add the character to the set.
        3. Return the longest_substring_len
        """
        l = 0
        longest_sub_len = 0
        current_set = set()

        for r in range(len(s)):
            while s[r] in current_set:
                current_set.remove(s[l])
                l += 1
            current_set.add(s[r])
            longest_sub_len = max(longest_sub_len, r-l+1)

        return longest_sub_len


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
