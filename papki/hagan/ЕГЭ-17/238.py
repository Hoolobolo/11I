s=[int(x) for x in open('17-1.txt')]
a=[]
for i in range(len(s)-2):
    s1=sum(s)/len(s)
    if int(s[i]<s1)+int(s[i+1]<s1)+int(s[i+2]<s1)>=2 and (abs(s[i])%100==14 or abs(s[i+1])%100==14 or abs(s[i+2])%100==14):
        a.append(s[i]+s[i+1]+s[i+2])
print(len(a),max(a))