class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize empty anagrams hash map (defaultdict(list))
        # For str in strs
        # - Initialize int array freq of length 26 (all zeros)
        # - For char in str
        #.   - freq[ord(char) - ord("a")] += 1
        # - anagrams[freq].append(str)
        # Return anagrams.values()
        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord("a")] += 1
            anagrams[tuple(freq)].append(s)
        return list(anagrams.values())