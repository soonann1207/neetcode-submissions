class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        sorted_map = sorted(hashmap.items(), key=lambda pair: pair[1], reverse = True)

        top_k = sorted_map[:k]

        return [i[0] for i in top_k]
        