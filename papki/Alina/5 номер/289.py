for x in range(1,1000):
    n=bin(x)[2:]
    if n.count('1')%2==0:
        n='1'+n+'00'
    else:
        n='11'+n
    r=int(n,2)
    if r>=412:
        print(x)
        break