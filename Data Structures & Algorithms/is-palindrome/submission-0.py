class Solution:
    def isPalindrome(self, s: str) -> bool:
        # In this expression str.isalnum checks whether the all char are str/num
        # filter(str.isalnum,s) keeps only str
        #.join joins them with an empty separator
        simple = ''.join(filter(str.isalnum,s)).lower() 
        return simple == simple[::-1]