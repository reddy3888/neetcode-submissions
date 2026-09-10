class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # creating a dictionary
        for s in strs:            # this loop iters on each individual string
            count = [0]*26        # create an arr with 26 zeros
            for c in s:            # creating a loop to iter each letter in a str
                count[ord(c) - ord('a')] += 1 # counts that char in the arr of 26 zeros
            ans[tuple(count)].append(s)        # this store the strings with same frequency pattern in the dictionary
        return list(ans.values())               # we return the same pattern in dictionary as list 