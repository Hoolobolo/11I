for i in range(0,1000):
    n=bin(i)[2:]
    if i%2==0:
        s=n.count('1')
        n=n+bin(s)[2:]
    else:
        n='1'+n+'00'
    r=int(n,2)
    if r>215:
        print(i)
        break