class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            frequencies = [0] * 26
            for char in s:
                frequencies[ord(char) - ord("a")] += 1
            
            frequencies = tuple(frequencies)

            anagrams[frequencies].append(s)
        
        res = []
        for group in anagrams.values():
            res.append(group)
        
        return res