class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "|" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        lower_pointer, upper_pointer = 0, 0

        while lower_pointer < len(s):
            upper_pointer = lower_pointer

            while s[upper_pointer] != "|":
                upper_pointer += 1

            print(s[lower_pointer:upper_pointer])
            length = int(s[lower_pointer:upper_pointer])

            lower_pointer = upper_pointer + 1
            upper_pointer = lower_pointer + length
            
            decoded.append(s[lower_pointer:upper_pointer])
            lower_pointer = upper_pointer

        return decoded
