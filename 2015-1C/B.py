from collections import defaultdict

def count_char(a,c):
	count = 0
	for i in range(len(a)):
		if c == a[i]: count+=1
	return count


def count_initial(w,V):
	Work = [0]*w # w - length of typing (s), V - word that we try to find
	j = 0
	count = 1
	i = 0
	for j in range(len(V)):
		Work[j] = V[j]
	if w < len(V): return 0
	if w == len(V): return 1
	for i in range(1,w - len(V)+1):
		check = 0
		if i+len(V)-1 < len(Work):
			for j in range(len(V)):
				if Work[i+j]!=V[j] and Work[i+j]!=0:
					check = 1
					break
				if Work[i+j] == 0 :
					Work[i+j] = V[j]
			if check == 0:
				count+=1
	return count


def solution(K,L,S,V,W):
	Voc = defaultdict(str)
	for i in range(len(V)):
		Voc[V[i]] = count_char(V,V[i])
	prob = 1
	for i in W:
		try:
			prob= prob*Voc[i]/len(V)
		except:
			return 0
	return (count_initial(S,W)-(S-len(W)+1)*prob)


N = int(input())

for n in range(1,N+1):
	K, L, S = map(int, input().split())
	V = str(input())
	W = str(input())
	Voc = defaultdict(str)
	for i in range(len(V)):
		Voc[V[i]] = count_char(V,V[i])
	print('Case #{}: {}'.format(n, solution(K,L,S,V,W)))
