class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            length = len(s)
            encoded_string +=  str(length) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        original_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i  = j + 1
            j = i + length
            original_strings.append(s[i:j])
            i = j
        return original_strings
