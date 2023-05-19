# Link:- https://www.codechef.com/LRNDSA01/problems/CONFLIP
for _ in range(int(input())):
    for _ in range(int(input())):
        i, n, q = map(int, input().split())
        if i == q:  
            print(n // 2)
        else:  
            print((n + 1) // 2)