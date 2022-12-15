class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        You are given a license key represented as a string s that consists of only alphanumeric characters and
        dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

        We want to reformat the string s such that each group contains exactly k characters, except for the first
        group, which could be shorter than k but still must contain at least one character. Furthermore, there must
        be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

        Return the reformatted license key.

        Input: s = "5F3Z-2e-9-w", k = 4
        Output: "5F3Z-2E9W"
        Explanation: The string s has been split into two parts, each part has 4 characters.
        Note that the two extra dashes are not needed and can be removed.

        Input: s = "2-5g-3-J", k = 2
        Output: "2-5G-3J"
        Explanation: The string s has been split into three parts,
        each part has 2 characters except the first part as it could be shorter as mentioned above.

        Constraints:

        1 <= s.length <= 10^5
        s consists of English letters, digits, and dashes '-'.
        1 <= k <= 10^4

        Plan:
        1. Sanitize the input to be all uppercase, and remove all of the dashes.
        2. Calculate the length of the first group, which is going to be len(sanitized_s) % k.
        3. Create the final array, and append the first group to the final array.
        4. Loop while i < len(sanitized_s), and append ("-" + k length slices of sanitized_s) to the final array.
        5. Join and return the final array.
        """
        sanitized_s = s.replace("-", "").upper()
        first_group_len = len(sanitized_s) % k
        if first_group_len == 0:
            first_group_len = k
        final_arr = [sanitized_s[:first_group_len]]

        i = first_group_len

        while i < len(sanitized_s):
            final_arr.append("-" + sanitized_s[i:i+k])
            i += k

        return "".join(final_arr)

result = Solution()
print(result.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(result.licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
