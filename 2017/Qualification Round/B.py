def convert(dt):
    d = map(str, dt)
    d = ''.join(d)
    d = int(d)
    return d

def solution(N):
    s = str(N)
    l=len(s)
    D = [0]*l
    e = 0
    for i in range(l):
        D[i]=int(s[i])
    for i in range(l-1):
        if D[i] < D[i+1]:
            e = i+1
        if D[i] > D[i+1]:
            D[e]-=1
            for j in range(e+1,l):
                D[j]=9
    if D[0] == 0: D.pop(0)
    return convert(D)



if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        f = input()
        print('Case #{}: {}'.format(n,solution(int(f))))
