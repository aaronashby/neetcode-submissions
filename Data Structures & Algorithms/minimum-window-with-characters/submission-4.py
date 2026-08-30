class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if s == t: return s

        countS, countT = {}, {}
        l = 0

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        need, have = len(countT), 0
        res, resLen = (-1, -1), float("infinity")
        
        for r in range(len(s)):
            if not s[r] in countT:
                continue
            else:
                countS[s[r]] = countS.get(s[r], 0) + 1

                if countS[s[r]] == countT[s[r]]:
                    have += 1

                while have == need:
                    if (r - l + 1) < resLen:
                        res = (l, r)
                        resLen = r - l + 1

                    if s[l] in countT:
                        countS[s[l]] -= 1
                        if countS[s[l]] < countT[s[l]]:
                            have -= 1
                    
                    l += 1
        
        return s[res[0] : res[1] + 1] if resLen != float("infinity") else ""
                    