from collections import defaultdict

N = int(input())
for n in range(1, N+1):
	S = str(input())
	res = str()
	D = defaultdict(int)
	for i in S:
		D[i]+=1
	z=[0]*10
	z[0] =D['Z']
	D['Z']-=z[0]
	D['E']-=z[0]
	D['R']-=z[0]
	D['O']-=z[0]
	z[2] = D['W']
	D['T']-=z[2]
	D['W']-=z[2]
	D['O']-=z[2]
	z[6] = D['X']
	D['S']-=z[6]
	D['I']-=z[6]
	D['X']-=z[6]
	z[7] = D['S']
	D['S']-=z[7]
	D['E']-=z[7]
	D['V']-=z[7]
	D['E']-=z[7]
	D['N']-=z[7]
	z[5] = D['V']
	D['F']-=z[5]
	D['I']-=z[5]
	D['V']-=z[5]
	D['E']-=z[5]
	z[4] = D['U']
	D['F']-=z[4]
	D['O']-=z[4]
	D['U']-=z[4]
	D['R']-=z[4]
	z[8] = D['G']
	D['E']-=z[8]
	D['I']-=z[8]
	D['G']-=z[8]
	D['H']-=z[8]
	D['T']-=z[8]
	z[1] = D['O']
	D['O']-=z[1]
	D['N']-=z[1]
	D['E']-=z[1]
	z[3] = D['T']
	D['T']-=z[3]
	D['H']-=z[3]
	D['R']-=z[3]
	D['E']-=z[3]
	D['E']-=z[3]
	z[9] = D['I']
	D['N']-=z[9]
	D['I']-=z[9]
	D['N']-=z[9]
	D['E']-=z[9]
	for i in range(len(z)):
		for j in range(z[i]):
			res+=str(i)
	print('Case #{}: {}'.format(n,res))
