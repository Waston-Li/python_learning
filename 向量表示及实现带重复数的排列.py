import numpy as np

e=np.array([0,1,2,3,4])#  numpy构建数组后转为向量
e.reshape(1,5) #一维行向量
k=0
for i in range(5):
    for j in range(5):
        for a in range(5):
            for b in range(5):
                for c in range(5):
                    print(e)
                    k+=1
                    e[1] = (e[1] + 1) % 5
                print(e)
                e[2] = (e[2] + 1) % 5
            print(e)
            e[3] = (e[3] + 1) % 5
        print(e)
        e[4] = (e[4] + 1) % 5
    print(e)
    e[0] = (e[0] + 1) % 5

print(k)