# Link:- https://www.codechef.com/problems/NUM239

for _ in range(int(input())):
    count = 0
    x, y = map(int, input().split())

    pretty_nums = ['2', '3', '9']
    for i in range(x, y+1):
        i = str(i)
        if i[-1] in pretty_nums:
            count += 1

    print(count)
