class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        d = "`"
        for s in strs:
            buff = s + d
            output.append(buff)
        return "".join(output)


    def decode(self, s: str) -> List[str]:
        output = []
        stri = []
        for c in s:
            if c != "`":
                stri.append(c)
            else:
                output.append("".join(stri))
                stri = []
        return output