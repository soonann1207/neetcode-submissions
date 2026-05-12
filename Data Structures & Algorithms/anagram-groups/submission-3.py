class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            # sort them 
            sorted_word = "".join(sorted(word))
            print(sorted_word)

            results[sorted_word].append(word)

        return list(results.values())
