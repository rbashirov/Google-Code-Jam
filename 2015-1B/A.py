def to_i(numList):
    s = ''.join(map(str, numList))
    return int(s)

def to_l(Num):
	return [int(x) for x in str(Num)]

def swap_n(a):
	for i in range(len(a)//2):
		tmp = a[i]
		a[i] = a[len(a) - i - 1]
		a[len(a) - i - 1] = tmp
	return(a)

def check_first_h(a):
	point = 0
	if (len(a)//2) > 1:
		for i in range(1,len(a)//2):
			if a[i] != 0: point = 1
	if point == 0 and a[0] == 1:
		return True
	else:
		return False

def solution(Num):
	count = 0
	a = to_l(Num)
	if a[len(a)-1]==0:
		a = to_l(int(Num)-1)
		count = 1
	while len(a)>1:
		if check_first_h(a):
			count = count + to_i(a[(len(a)//2):]) + 1
		else:
			count = count + to_i(a[(len(a)//2):]) + to_i(swap_n(a[:len(a)//2]))+1
		a=[9 for i in range(len(a)-1)]

	count+=to_i(a)
	return count

N = int(input())

for n in range(1,N+1):
	Num = int(input())
	print('Case #{}: {}'.format(n, solution(Num)))
