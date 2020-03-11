class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return
        # bigO of n?
        wordDict = {}
        for word in strs:
            d = [0]*26
            for ltr in word:
#               get id of word via letter counting
                d[ord(ltr) - ord('a')] += 1
            # repr(d) is the key for our outer dictionary
            if repr(d) in wordDict:
                wordDict[repr(d)].append(word)
            else:
                wordDict[repr(d)] = [word]
        home = []
        for k in wordDict:
            home.append(wordDict[k])
        print(home)
        return home
    