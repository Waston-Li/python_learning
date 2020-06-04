import numpy as np
import matplotlib.pyplot as plt

# https://www.runoob.com/w3cnote/matplotlib-tutorial.html
#https://www.runoob.com/numpy/numpy-matplotlib.html


#histogram直方图 plt.hist()的用法: https://zhuanlan.zhihu.com/p/37959111
a, b = (-5, 5)
fig = plt.figure(figsize=(10, 8))

rvs = np.random.rand(10000) * (b - a) + a  # 产生10k个数存到列表中

n, bins,_= plt.hist(rvs, bins=20, range=(a, b), normed=True, facecolor='blue', label='hist of generated data')

plt.plot(bins, np.ones_like(bins) / (b - a), 'r--', label='density function U[-5,5]')

plt.ylabel("frequency or density", fontsize=15)
plt.xlabel("domain of density function", fontsize=15)
plt.title(r'generated 10000 rvs from U[-5,5]', fontsize=15)

plt.legend(loc=1)

plt.show()
