class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0

        while i < len(s):
            wordLen = ""
            word = ""

            while s[i] != "#":
                wordLen += s[i]
                i += 1
            wordLen = int(wordLen)

            for j in range(wordLen):
                i += 1
                word += s[i]
            decoded.append(word)
            i += 1
        
        return decoded
            