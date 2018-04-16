def solution(N,S):
    odd = [0]*(int(N/2)+N%2)
    even = [0]*int(N/2)
    sorted_s = [0]*N
    for i in range(N):
        if i%2 == 0:
            odd[int(i/2)] = int(S[i])
        else:
            even[int(i/2)] = int(S[i])
        sorted_s[i] = int(S[i])
    odd.sort()
    even.sort()
    sorted_s.sort()
    for i in range (N):
        if i%2 == 0:
            if odd[int(i/2)] != sorted_s[i]:
                return i
        else:
            if even[int(i/2)] != sorted_s[i]:
                return i
    return 'OK'

if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        f = int(input())
        s = input().split()
        print('Case #{}: {}'.format(n,solution(f,s)))
