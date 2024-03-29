class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        https://leetcode.com/problems/longest-repeating-character-replacement/

        You are given a string s and an integer k.
        You can choose any character of the string and change it to any other uppercase English character.
        You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above
        operations.

        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.

        Constraints:

        1 <= s.length <= 105
        s consists of only uppercase English letters.
        0 <= k <= s.length

        Plan:
        No idea
        '''

        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result

        # Neetcode
        # count = {}
        #         res = 0
        #
        #         l = 0
        #         maxf = 0
        #         for r in range(len(s)):
        #             count[s[r]] = 1 + count.get(s[r], 0)
        #             maxf = max(maxf, count[s[r]])
        #
        #             if (r - l + 1) - maxf > k:
        #                 count[s[l]] -= 1
        #                 l += 1
        #
        #             res = max(res, r - l + 1)
        #         return res

        # Neetcode Easier
        # count = {}
        # res = 0
        #
        # left = 0
        # max_freq = 0
        # for right in range(len(s)):
        #     count[s[right]] = 1 + count.get(s[right], 0)
        #
        #     while (right - left + 1) - max(count.values()) > k:
        #         count[s[left]] -= 1
        #         left += 1
        #
        #     res = max(res, right-left+1)
        # return res
