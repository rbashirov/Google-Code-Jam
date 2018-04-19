N = int(input())

for n in range(1,N+1):
	R, C, W = map(int,input().split())
	if C%W == 0:
		res = C//W*R + W -1
	else:
		res = C//W*R + W
	print('Case #{}: {}'.format(n, res))
