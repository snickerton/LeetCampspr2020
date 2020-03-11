s = "PAYPALISHIRING"
numRows = 4
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#PAYPALISHIRING
#P-----I-----N-
#-A---L-S---I-G
#--Y-A---H-R---
#---P-----I----
#12343212343212
#01232101232101 
place = 0
everything = [[] for x in range(numRows)]
for i in range(len(s)):
    if place == numRows-1:
        #countdown
        adder = -1;
    if place == 0:
        #countup
        adder = 1;
    everything[place].append(s[i])
    place += adder

print(everything)
book = ''.join([''.join(x) for x in everything])
print(book)