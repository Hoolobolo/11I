with open("17-1.txt") as f:
    a = [int(x) for x in f]
c=[]
count=0
b=sum(a)/len(a)
for i in range(len(a)-2):
    if (a[i]<b or a[i+1]<b or a[i+2]<b) and (str(a[i]).count('9')>=1 and str(a[i+1]).count('9')>=1 and str(a[i+2]).count('9')>=1):
        c.append((a[i]+a[i+1]+a[i+2]))
        count+=1
print(count,max(c))