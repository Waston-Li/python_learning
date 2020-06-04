def pri_num(n):
    for i in range(2, n):
        for j in range(2, i):
            if (i % j == 0):
                print(i, '=', j, '*', i // j)
                break  # 此处加了break才会避免执行接下来的else
        else:
            print(i, '是质数')

dic=['dasda',1]