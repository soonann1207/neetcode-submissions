class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        hashmap = {}
        for i in strs:
            sorted_text = "".join(sorted(i))
            if sorted_text not in hashmap:
                hashmap[sorted_text] = []
            hashmap[sorted_text].append(i)

        return list(hashmap.values())