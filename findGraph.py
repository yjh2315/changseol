def findTilt():
    rep = int(input("반복할 횟수:"))

    x= []
    y= []

    for k in range(rep):
        tmp = input()
        tmp2 = tmp.split(' ')
        x.append(int(tmp2[0]))
        y.append(int(tmp2[1]))

    tilt = 0
    val = 10000000000000000000000000000

    for i in range(10000):
        k = i/100
        up = 0
        for j in range(rep):
            up += abs(k*x[j]-y[j])
        tmp = up/pow(k**2+1,1/2)
        
        if tmp<val:
            val = tmp
            tilt = k

    return tilt,val

def findY(tilt,x):
    return tilt*x