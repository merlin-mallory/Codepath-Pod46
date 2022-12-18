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
        1. Create a substring_set(initialized to s[0]), l = 0, r = 1, current_len, max_len.
        2. While r <= len(s)-1:
            3. if s[r] not in substring_set:
                4. substring_set.add(s[r]), r+1, current_len+1, update max_len.
            5. else:
                6. substring_set.remove(s[l])
                7. l += 1, current_len-1
        8. Return max_len
        """
        l, r = 0, 0
        substring_set = set()
        current_len, max_len = 0, 0

        while r <= len(s)-1:
            if s[r] not in substring_set:
                substring_set.add(s[r])
                r += 1
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                substring_set.remove(s[l])
                l += 1
                current_len -= 1

        return max_len


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
