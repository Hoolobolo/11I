a=[int(x) for x in open("17-205.txt")]
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1-n2)%2==0 and (n1-n2)%37==0:
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)