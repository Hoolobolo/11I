s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    s1=sum(s)/len(s)
    if (s[i]<s1 or s[i+1]<s1 or s[i+2]<s1) and (int(abs(s[i])%10==4)+int(abs(s[i+1])%10==4)+int(abs(s[i+2])%10==4)>=2):
        a.append(s[i]+s[i+1]+s[i+2])
print(len(a),max(a))