a=[int(x) for x in open("17-243.txt")]
soom=0
for x in a:
	if x%49==0:
		for i in str(x):
			soom+=int(i)
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1<soom and n2>=soom and n2%13==0) ^ (n2<soom and n1>=soom and n1%13==0):
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)