import numpy as np
N =10000

def alg():
    sum1=0
    a=[]
    for _ in range(1, 1000):
        for _ in range(1, N):
            U = np.random.rand(5)
            X = -np.log(U)
            sum = X[0] + 2 * X[1] + 3 * X[2] + 4 * X[3] + 5 * X[4]
            if (sum > 21.6):
                sum1 += 1
            else:
                sum1 = 0
        theta = sum1 / N
        a.append(theta)
    print(np.mean(a))
for _ in range(5):
    alg()