# Link:- https://www.codechef.com/problems/FLOW017

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a>b:
        if a>c:
            print(max(b,c))
        else:
            print(a)
    elif b>c:
        print(max(a,c))
    else:
        print(b)