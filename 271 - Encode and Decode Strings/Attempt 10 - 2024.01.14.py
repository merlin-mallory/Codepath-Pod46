class Codec:
    """
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
      //... your code
      return strs;
    }
    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.

    You are not allowed to solve the problem using any serialize methods (such as eval).

    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    Example 2:

    Input: dummy_input = [""]
    Output: [""]

    Encoding Plan:
    1. Choose special characters to encode the end of each string.
    2. Loop through each string in strs, and append to encoded_str.
    3. Return the result.

    Decoding Plan:
    1. Loop through each char of the encoded string, add each char to a temporary array. When we hit the special
    character, and push the contents of the temp_array to the decoded_array. Then clear the temp array, and skip over
    the special character.
    2. Return the decoded_array.
    """

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Encode with str_len + "#" + str.
        """
        final_str = []
        for string in strs:
            final_str.append(str(len(string)) + "#" + string)
        return ''.join(final_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. While there is an int, move right until we reach the #, collecting the integers. Convert that str into an
        int. Then move +1 index, and slice according to the length of the str. Append that string to the final array.
        Keep going until we reach the end of the string. Then join and return the final answer.
        """
        len_of_s = len(s)
        i = 0
        final_arr = []
        while i < len_of_s:
            len_substring = ""
            while s[i] != "#":
                len_substring += s[i]
                i += 1
            len_substring = int(len_substring)

            i += 1

            substring = s[i:(i + len_substring)]
            final_arr.append(substring)
            i += len_substring
        return final_arr



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
