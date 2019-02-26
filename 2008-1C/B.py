def solution(r):
    MOD = 210
    din = [[0] * 210 for i in range(41)]
    din[0][0] = 1
    for i in range(len(r)):
        numt = 0 
        for j in range(i,len(r)):
            numt = (numt*10 + r[j])
            for x in range(210):
                if i == 0:
                    din[j+1][(x+numt)%MOD] += din[i][x]
                if i > 0:
                    if x-numt < 0:
                         din[j+1][(x+numt)%MOD]+=din[i][x]
                         din[j+1][(-x+numt)%MOD]+=din[i][x]
                    else:
                         din[j+1][(x+numt)%MOD]+=din[i][x]
                         din[j+1][(x-numt)%MOD]+=din[i][x]

    res = 0
    for i in range(210):
        if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 == 0:
            res+=din[len(r)][i]
    return res


if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        r = [int(i) for i in str(input())]
        print('Case #{}: {}'.format(n,solution(r)))
