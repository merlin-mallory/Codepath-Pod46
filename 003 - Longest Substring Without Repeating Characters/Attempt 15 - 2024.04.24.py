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
        Time: O(n)
        Space: O(n)
        Edge: Could be 0 len
        """
        s_set = set()
        len_of_longest_substring = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in s_set:
                s_set.add(s[r])
            else:
                while s[r] in s_set:
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
