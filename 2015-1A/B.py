def served_customers(T, B, M):
	if T<0: return 0
	served = 0
	for i in range(B):
		served+=T//M[i] + 1
	return served

def solution(B,M,place):
	high = 1000000000000*B
	low = -1
	while low + 1 < high:
		mid = (high+low)//2
		if served_customers(mid,B,M) < place:
			low = mid
		else:
			high = mid
	T = high
	served_before = served_customers(T-1,B,M)
	srv = served_customers(T,B,M)
	#return srv
	for i in range(B):
		if T%M[i] == 0:
			served_before+=1
			if served_before == place:
				return (i+1)
N = int(input())

for n in range(1,N+1):
	B, place = map(int, input().split())
	M = list(map(int, input().split()))
	print('Case #{}: {}'.format(n, solution(B,M,place)))
