def conv(x,y):
	summ=0
	while x>0:
		summ+=x%y
		x//=y
	return summ
a=[int(x) for x in open("17-282.txt")]
cnt=0
mix=20000
soom=10000
for x in a:
	if x%21==0:
		soom=min(soom,x)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	sum7=conv(soom,8)
	if conv(n1,8)==sum7 or conv(n2,8)==sum7:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)