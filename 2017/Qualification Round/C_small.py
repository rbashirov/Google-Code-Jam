import heapq

def solution(f,s):
    h = [-f]
    heapq.heapify(h)
    for i in range (s-1):
        tmp = - int(heapq.heappop(h))
        heapq.heappush(h,-int((tmp-1)/2))
        heapq.heappush(h,-(tmp - 1 - int((tmp-1)/2)))
    tmp = - heapq.heappop(h)
    return [max(int((tmp-1)/2),(tmp - 1 - int((tmp-1)/2))), min(int((tmp-1)/2),(tmp - 1 - int((tmp-1)/2)))]

if __name__ == "__main__":
    t = int(input())
#    print(t)
    for n in range(1,t+1):
        f,s = input().split()
#        print(f,s)

        res = solution(int(f),int(s))
        print('Case #{}: {} {}'.format(n,res[0],res[1]))
