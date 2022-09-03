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
        1. Initialize left to 0. Create an added_set. max_len = 0. current_len =

        '''
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

        # Failed Attempt
        # added_set = set()
        # max_len = 0
        #
        # for i in range(len(s)):
        #     current_val = s[i]
        #     left = i
        #     right = i
        #     added_set.add(current_val)
        #     temp_k = k
        #     while temp_k >= 1 and right < len(s):
        #         if s[right] not in added_set:
        #             added_set.add(s[right])
        #             right += 1
        #         else:
        #             added_set.add(s[right-1])
        #             s = s[:right] + s[right-1] + s[right+1:]
        #             temp_k -= 1
        #     max_len = max(max_len, right-left+1)

        return max_len


result = Solution()
print(result.characterReplacement("ABAB", 2))  # 2
print(result.characterReplacement("AABABBA", 1))  # 4

