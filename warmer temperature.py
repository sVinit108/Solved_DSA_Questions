# Link:- https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n=len(temps)
        ans=[-1]*(n)
        j=0
        i=1
        curr_temp=temps[0]
        count=0
        while(True):
            if ans[-1]!=-1:
                break
            else:
                if i<n:
                    for k in temps[i:]:
                        if k>curr_temp:
                            ans[j]=count+1
                            curr_temp=temps[i]
                            count=0
                            break
                        else:
                            count+=1
                    if(ans[j]==-1):
                        ans[j]=0
                        count=0
                        curr_temp=temps[i]
                    i+=1
                    j+=1
                else:
                    ans[j]=0
        
        return ans