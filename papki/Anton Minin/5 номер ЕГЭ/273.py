for i in range(1000):
    n=bin(i)[2:]
    if i%2!=0:
        n='1'+n+'0'
    else:
        n='11'+n+'11'
    r=int(n,2)
    if r<126:
        print(r)
        
        
# работает
