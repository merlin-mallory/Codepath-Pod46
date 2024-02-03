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
        Hashmap
        1. Create s_set, init empty.
        2. Init len_of_longest_substring
        3. l = 0, r = 0.
        4. While r < len(s)
            5. Check if there's a set and s[r] is in the set. If so, remove s[l], and increment l until that is no
            longer the case. Otherwise, add s[r] to the set.
            6. Update len_of_longest_substring.
        7. Return len_of_longest_substring
        Time: O(n)
        Space: O(n)
        Edge: len(s) == 0, return "".
        """
        s_set = set()
        len_of_longest_substring = 0
        l, r = 0, 0
        while r < len(s):
            while s_set and s[r] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[r])
            len_of_longest_substring = max(len_of_longest_substring, len(s_set))
            r += 1
        return len_of_longest_substring


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
