# Link:- 

n=int(input())
lt=list(map(int,input().split()))
luck=0
for i in range(n):
    if (lt[i]%2==0):
        luck=luck+1
 
if (luck> n-luck):
    print("READY FOR BATTLE")
else:
    print("NOT READY")