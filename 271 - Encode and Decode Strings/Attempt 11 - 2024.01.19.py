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
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Plan:
        Array
        1. Initialize encoded_str as an array. Loop through strs. Calculate each string's length. Encode the length
        of a string + string + "#" sign, and append to encoded_str.
        2. Join and return encoded_str.
        """
        encoded_str = []
        for substring in strs:
            substring_len = len(substring)
            encoded_str.append(str(substring_len) + "#" + substring)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        1. Initialize decoded_str as an array. Loop through s. Analyze the int at the beginning of the list. Slice s to
        grab the substring, and append to decoded_str. Advance pointer past the "#" sign, and repeat until end of
        string.
        2. Return decoded_str.
        """
        decoded_str = []
        i = 0
        while i < len(s):
            len_substring = ""
            while s[i] != "#":
                len_substring += s[i]
                i += 1
            len_substring = int(len_substring)

            i += 1

            substring = s[i:(i + len_substring)]
            decoded_str.append(substring)
            i += len_substring
        return decoded_str


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
