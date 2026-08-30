class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        l = 0

        for c in s1:
            s1_count[ord(c) - ord("a")] += 1
        
        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord("a")] += 1

            if s1_count == s2_count:
                return True
            
            if (r - l + 1) == len(s1):
                s2_count[ord(s2[l]) - ord("a")] -= 1
                l += 1
        return False