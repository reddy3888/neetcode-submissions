class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # we count the frequency of the nums

        buckets = [[] for _ in range(len(nums) + 1)] # creates one bucket for each possible freq

        # now we should assign the num to that freq

        for num, freq in count.items(): # count.items() give value -> freq
            buckets[freq].append(num)
        
        result = []

        # we are starting from the highest freq
        for freq in range(len(buckets) - 1, 0, -1): # it gives bucket[3] which is [1]
            for num in buckets[freq]:                # we need the num in it
                result.append(num)                  # add the high freq num to res

            if len(result) == k:                    # after getting the required list of num we return tha result
                return result