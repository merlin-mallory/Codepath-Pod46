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
        1. Loop through each char in the string. Each iteration will be a starting point.
        2. While a duplicate is not found, add the char to set and increase the current_len by 1. Eventually if a
        duplicate is found, or we've reached the end of the array, set the max of current_len and max_len.
        3. Time: O(n^2), Space: O(n)
        """
        # So my initial attempt worked, but it's brute force instead of sliding window. Here's the O(n) time O(n)
        # space sliding window solution

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        # if not s:
        #     return 0
        #
        # max_len = 0
        # for i in range(len(s)):
        #     chars_in_set = set()
        #     current_len = 0
        #     start_char = s[i]
        #     j = i
        #     while j <= len(s)-1:
        #         current_val = s[j]
        #         if current_val not in chars_in_set:
        #             current_len += 1
        #             chars_in_set.add(s[j])
        #             j += 1
        #         else:
        #             break
        #     max_len = max(max_len, current_len)
        # return max_len


result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))  # 1
print(result.lengthOfLongestSubstring("pwwkew"))  # 3
