a=[int(x) for x in open("17-1.txt")]
cnt=0
mix=0
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	avg=sum(a)/len(a)
	if (n1<avg or n2<avg or n3<avg) and (str(n1).count("8")>=1 or str(n2).count("8")>=1 or str(n3).count("8")>=1):
			cnt+=1
			mix=max(mix,n1+n2+n3)
print(cnt,mix)