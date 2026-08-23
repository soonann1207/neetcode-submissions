from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)

        # hashmap_s = {}
        # hashmap_t = {}

        # for i in s:
        #     if i not in hashmap_s:
        #         hashmap_s[i] = 1
        #     else:
        #         hashmap_s[i] += 1
        

        # for i in t:
        #     if i not in hashmap_t:
        #         hashmap_t[i] = 1
        #     else:
        #         hashmap_t[i] += 1
        

        # return hashmap_s == hashmap_t
        