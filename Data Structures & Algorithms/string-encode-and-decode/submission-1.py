class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for string in strs:
            final += str(len(string)) + "!" + string
        
        return final

    def decode(self, s: str) -> List[str]:
        final = []
        while s != "":
            splitted = s.split("!", 1)
            lenStr = int(splitted[0])
            text = splitted[1][0:lenStr]

            final.append(text)
            s = splitted[1][lenStr:]
        return final
