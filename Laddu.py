# Link:- https://www.codechef.com/LRNDSA01/problems/LADDU

for _ in range(int(input())):
    points = 300
    activities, origin = input().split()
    
    for i in range(int(activities)):
        act, *pts = input().split()
        
        if len(pts) != 0:
            pt = int(pts[0])
            if act == "CONTEST_WON" and pt <= 20:
                bonus = 20 - pt
                points += bonus
            if act == "BUG_FOUND":
                points += pt
        if act == "TOP_CONTRIBUTOR":
            points += 300
        if act == "CONTEST_HOSTED":
            points += 50
    
    if origin == "INDIAN":
        print(points // 200)
    else:
        print(points // 400)
