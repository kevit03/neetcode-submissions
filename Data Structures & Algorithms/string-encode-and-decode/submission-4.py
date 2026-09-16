class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(item)) + "#" + item for item in strs)

    def decode(self, s: str) -> List[str]:
        new_list = []

        while s:
            ind = s.index("#")
            length = int(s[:ind])

            start = ind + 1
            word = s[start:start + length]

            new_list.append(word)
            s = s[start + length:]

        return new_list