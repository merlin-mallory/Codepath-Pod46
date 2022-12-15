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
        1. Create encoded_arr. Loop through strs. Calculate len(my_str). Append (len(my_str)+"#"+my_str).
        2. Join and return encoded_arr as a string.
        """
        encoded_arr = []
        for my_str in strs:
            encoded_arr.append(str(len(my_str)) + "#" + my_str)
        return "".join(encoded_arr)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        1. Create decoded_arr. Loop through char in s. The zero index will be a number. Iterate forward until we see
        the pound sign. Then convert that number to an int. Then slice from i+1 to i+1+length. Append that slice to
        decoded_arr. Iterate to the next number, and repeat until we've reached the end of the string.
        2. Return decoded_arr.
        """
        decoded_arr = []
        length_arr = []

        i = 0
        while i < len(s):
            length_arr = []
            while s[i] != "#" and i < len(s):
                length_arr.append(str(s[i]))
                i += 1
            length = int("".join(length_arr))
            decoded_arr.append(s[i+1:(i+1+length)])
            i += 1 + length
        return decoded_arr




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
