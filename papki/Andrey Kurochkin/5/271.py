for k in range(1,1000):
    i=k
    n=''
    while i:
        n=str(i%4)+n
        i//=4
    if k%2!=0:
        n='2'+n+'11'
    else:
        n='13'+n+'02'
    r=int(n,4)
    if r>1000:
        print(r)
        break
    
    