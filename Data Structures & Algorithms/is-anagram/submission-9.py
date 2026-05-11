class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}

        for i in list(s):
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1

        for i in list(t):
            if i not in b.keys():
                b[i] = 1
            else:
                b[i] += 1

        return a == b