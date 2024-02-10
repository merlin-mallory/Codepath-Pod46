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
        Create s_set, init empty, l = 0, r = 0, len_of_longest_substring = 0
        Loop through s.
            If s[r] is in s_set, then iteratively remove s[l] and l++, until s[r] is no longer in s_set. Then add s[
            r] to s_set, and r++.
            Otherwise, add s[r] to s_set, and r++, and update len_of_longest_substring
        Return len_of_longest_substring.
        """
        s_set = set()
        len_of_longest_substring = 0
        l, r = 0, 0
        while r < len(s):
            while s_set and s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            len_of_longest_substring = max(len_of_longest_substring, r-l+1)
            r += 1
        return len_of_longest_substring


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
