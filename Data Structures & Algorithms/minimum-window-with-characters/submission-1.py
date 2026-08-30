class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t): return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        l = 0
        res = ((0, 0), 0)
        have, need = 0, len(countT.values())

        for r in range(len(s)):
            if not countT.get(s[r], 0):
                continue
            else:
                window[s[r]] = window.get(s[r], 0) + 1
                
                if window[s[r]] == countT[s[r]]:
                    have += 1
                
                if have == need:
                    while have == need:
                        if countT.get(s[l], 0):
                            window[s[l]] -= 1
                            if window[s[l]] < countT[s[l]]:
                                have -= 1
                        if res[1] == 0 or (r - l + 1) < res[1]:
                            res = ((l, r), r - l + 1)

                        l += 1
        if res[1] > 0:
            return s[res[0][0]:res[0][1] + 1]
        else:
            return ""