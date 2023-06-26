#Link:- https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        ref_table={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        count = 0
        for i in range(len(s)):
            if s[i]!="I":
                temp=s[i]
                val = ref_table[temp]
                count+=val
            else:
                count+=1
            if i<(len(s)-1):
                if s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X"):
                    count-=2

                if s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C"):
                    count-=20

                if s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M"):
                    count-=200

        return count