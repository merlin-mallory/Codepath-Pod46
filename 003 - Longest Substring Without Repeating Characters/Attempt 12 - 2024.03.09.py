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
        Create s_set.
        Init longest_substring_len to 0.
        l, r = 0, 0
        Loop through s.
            Loop while s[r] is in s_set. Remove s[l] from s_set and l++.
            Add s[r] to s_set, and update longest_substring_len.
        Return longest_substring_len.
        """
        s_set = set()
        longest_substring_len = 0
        l, r  = 0, 0
        while r < len(s):
            while s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            longest_substring_len = max(longest_substring_len, r-l+1)
            r += 1
        return longest_substring_len


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
