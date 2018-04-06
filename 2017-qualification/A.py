def check(p,f):
    for ch in range(p,len(f)):
        if f[ch] == '-':
            return False
    return True

def solution(f,s):
    d = {'+':'-','-':'+'}
    l = len(f)
    res = 0
    if len(f) < s:
        return 'IMPOSSIBLE'
    for i in range(0,l):
        if f[i]=='-':
            res+=1
            for p in range(s):
                f[p+i] = d[f[p+i]]
        if i>= (l-s):
            if check(i,f):
                return res
            else:
                return 'IMPOSSIBLE'
    return res


t = int(input())
for n in range(1,t+1):
    f,s = input().split()
    print('Case #{}: {}'.format(n,solution(list(f),int(s))))
