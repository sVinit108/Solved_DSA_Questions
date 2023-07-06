#Link:- https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count=0
        dividend1=abs(dividend)
        divisor1=abs(divisor)
        if divisor1 == 1 and dividend1!=0:
            count=dividend1
        else:
            while(True):
                if dividend1>=divisor1:
                    dividend1-=divisor1
                    count+=1
                else:
                    break
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0) :
            return -count
        else:
            return count