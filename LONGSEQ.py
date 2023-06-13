# Link:- https://www.codechef.com/problems/LONGSEQ

for i in range(int(input())):
    num = list(map(int,input()))
    if len(num) == sum(num) + 1:
        print("Yes")
    elif sum(num)==1:
        print("Yes")
    else:
        print("No")