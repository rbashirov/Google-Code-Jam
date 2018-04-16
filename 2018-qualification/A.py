def score(P):
    current = 1
    result = 0
    for i in range(len(P)):
        if P[i] == 'S': result+=current
        if P[i] == 'C': current = current*2
    return result

def swap(P):
    num_c = 0
    P = list(P)
    for i in reversed(range(1,len(P))):
        if P[i-1] == 'C' and P[i] == 'S':
            P[i-1], P[i] = P[i], P[i-1]
            return P
    return False

def solution(D,P):
    D=int(D)
    count = 0
    if len([x for x in P if x == 'S']) == 0:
        return 0
    if len([x for x in P if x == 'S']) > D:
        return 'IMPOSSIBLE'
    while True:
        if score(P) <= D:
            return count
        else:
            P = swap(P)
            count+=1
    return count

if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        f,s = input().split()
        print('Case #{}: {}'.format(n,solution(f,s)))
