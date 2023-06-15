# Link:- https://www.codechef.com/problems/IPCCERT

n,m,k = map(int,input().split())
count=0
for _ in range(k):
    *lec,q = map(int,input().split())
    if sum(lec)>=m and q<=10:
        count+=1
print(count)