def solution(P,K,L,M):
    M.sort(reverse=True)
    res = 0
    for i in range(len(M)):
        num = i//K + 1
        res+=num*M[i]
    return res

if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        P,K,L = map(int, input().split())
        M = list(map(int, input().split()))
        print('Case #{}: {}'.format(n,solution(P,K,L,M)))
