from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            # Sort the word and use it as the key
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())