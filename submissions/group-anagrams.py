class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = dict()

        for word in strs:

            counts = [0] * 26
            for letter in word:
                index = ord(letter) - ord("a")
                counts[index] += 1

            counts = tuple(counts)
            anagrams.setdefault(counts, [])
            anagrams[counts].append(word)

        return list(anagrams.values())
