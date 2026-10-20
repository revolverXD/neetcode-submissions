class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angram_set = set()
        angram_dict = {}

        for s in strs:
            angram_set.add("".join(sorted(s)))
        for s in angram_set:
            angram_dict[s] = []
        
        for word in strs:
            angram_form = "".join(sorted(word))
            angram_dict[angram_form].append(word)
        return [angram_dict[w] for w in angram_dict]

