a=[int(x) for x in open("17-243.txt")]
max19=0
for x in a:
	if x%119==0:
		max19=max(max19,x)
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1<max19 and n2<max19):
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)