def max_place(S):
	m = max([x for x in S])
	for i in range(len(S)):
		if m == S[i]: return i

def solution(S):
	res = str()
	res = S[0]
	for i in range(1,len(S)):
		if max(res[0],S[i]) == S[i]:
			res = S[i]+res
		else:
			res+=S[i]
	return res

N = int(input())
for n in range(1,N+1):
	S = str(input())
	print('Case #{}: {}'.format(n,solution(S)))
