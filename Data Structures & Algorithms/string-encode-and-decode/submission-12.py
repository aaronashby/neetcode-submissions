class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        l, r = 0, 1
        
        res = []
        
        while l < len(s):
            while s[r] != "#":
                r += 1
            
            length = int(s[l:r])
            l = r + 1
            r = l + length

            res.append(s[l:r])

            l = r
            r += 1
        
        return res