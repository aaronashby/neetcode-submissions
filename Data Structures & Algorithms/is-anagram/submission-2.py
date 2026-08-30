class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequencies = dict()

        for letter in s:
            if ord(letter) not in frequencies:
                frequencies[ord(letter)] = 1
            else:
                frequencies[ord(letter)] += 1
        
        for letter in t:
            if ord(letter) not in frequencies:
                return False
            else:
                frequencies[ord(letter)] -= 1
        
        for frequency in frequencies.values():
            if frequency != 0:
                return False
        
        return True