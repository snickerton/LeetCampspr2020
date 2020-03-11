class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#      instead of using a dict let's just use an array that's indexed by the ascii value from a
#      example: a-a = index 0,  f-a = index 5
        d = [0]*(ord('z')-ord('a')+1)
        print(len(d))
#         tolower everything to check for edge cases of weird inputs
        rNFixed = ransomNote.lower()
        mag = magazine.lower()
        for x in mag:
            key = ord(x)-ord('a')
#             same thing about checking inputs
            if(key>26):
                print("not a letter")
            d[key] += 1
        for x in rNFixed:
            key = ord(x)-ord('a')
            d[key] -= 1
            if d[key] < 0:
                return False
        
        return True
                    