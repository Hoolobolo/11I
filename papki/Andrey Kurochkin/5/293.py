for m in range(1,10000):
    p1=p2=1
    d=[int(c) for c in str(m)]
    for c in d:
        if c%2==0 and c>0:
            p1=p1*c
        if c%2!=0:
            p2=p2*c
    p1=p1*2
    r=abs(p2-p1)
    if r==29:
        print(m)