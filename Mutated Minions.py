# Link:- https://www.codechef.com/problems/CHN15A

for _ in range(int(input())):
    n,k = map(int,input().split())
    nums = list(map(int,input().split()))
    count=0
    for i in range(n):
        nums[i]+=k
        if nums[i]%7==0:
            count+=1        
    print(count)