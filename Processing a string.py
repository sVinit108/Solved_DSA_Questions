# Link:- https://www.codechef.com/problems/KOL15A

for _ in range(int(input())):
    count=0
    s=input()
    for i in s:
        if i.isdigit():
            count+=int(i)
    print(count)