with open("17-1.txt") as f:
    a = [int(x) for x in f]
count=0
c = []
s = sum(a)/len(a)
for i in range(len(a)-1):
    if (a[i]<s or a[i+1]<s) and ((a[i]%3==0 and a[i]%5!=0 and a[i]%11!=0 and a[i]%19!=0) or (a[i+1]%3==0 and a[i+1]%5!=0 and a[i+1]%11!=0 and a[i+1]%19!=0)) :
        count+=1
        c.append(a[i]+a[i+1])
print(count,max(c))