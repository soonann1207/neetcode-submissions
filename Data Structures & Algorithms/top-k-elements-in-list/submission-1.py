class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_count_dict = {}
        for num in nums:
            if num not in number_count_dict:
                number_count_dict[num] = 1
            else:
                number_count_dict[num] += 1

        # sort dictionary 
        sorted_dict = sorted(number_count_dict.items(), key=lambda x:x[1], reverse=True)

        # return top k 
        results = sorted_dict[:k]

        return [i[0] for i in results]