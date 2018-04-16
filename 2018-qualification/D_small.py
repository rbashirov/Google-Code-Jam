from math import *

if __name__ == "__main__":
    t = int(input())
    for n in range(1,t+1):
        f = float(input())
        x=[0]*3
        y=[0]*3
        z=[0]*3
        my_cos = f/(2**0.5)
        alpha_u = acos(my_cos) + pi/4
        alpha_d = pi/4 - acos(my_cos)
        x[0] = sin(alpha_u)*0.5
        x[1] = cos(alpha_u)*0.5
        y[0] = -1*sin(alpha_d)*0.5
        y[1] = cos(alpha_d)*0.5
        z[2] = 0.5
        print('Case #{}:'.format(n))
        print('{} {} {}'.format(x[0],x[1],x[2]))
        print('{} {} {}'.format(y[0],y[1],y[2]))
        print('{} {} {}'.format(z[0],z[1],z[2]))
