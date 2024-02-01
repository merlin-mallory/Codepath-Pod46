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
        1. Init encoded_str = []
        2. Loop through strs
            3. Append (len(cur_str) + "#" + cur_str)
        """
        encoded_str = []
        for cur_str in strs:
            encoded_str.append(str(len(cur_str)) + "#" + cur_str)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            temp_len = []
            while s[i].isdigit():
                temp_len.append(s[i])
                i += 1
            cur_len = int(''.join(temp_len))

            i += 1

            cur_str = s[i: i+cur_len]
            decoded_strs.append(cur_str)
            i += cur_len

        return decoded_strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
