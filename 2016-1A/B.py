from collections import defaultdict

N = int(input())
 
for n in range(1,N+1):
	matr = []
	res = []
	size = int(input())
	for i in range(2*size-1):
		matr+=[x for x in map(int,input().split())]
	D = defaultdict(int)
	for i in matr:
		D[i]+=1
	for i in D:
		if D[i]%2 == 1:
			res.append(i)
	res.sort()
	result = ' '.join(str(x) for x in res)
	print('Case #{}: {}'.format(n,result))
