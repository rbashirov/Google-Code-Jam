if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        q = int(input())
        X = [int(x) for x in input().split()]
        a = sum([max(0,X[i-1] - X[i]) for i in range(1,q)])
        m = max([max(0,X[i-1] - X[i]) for i in range(1,q)])
        b = sum([min(X[i],m) for i in range(q-1)])
        print('Case #{}: {} {}'.format(n,a,b))
