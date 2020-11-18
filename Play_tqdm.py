from tqdm import tqdm
import time

# https://www.jb51.net/article/166648.htm
# Tqdm
# 是一个快速，可扩展的Python进度条，可以在Python
# 长循环中添加一个进度提示信息，用户只需要封装任意的迭代器tqdm(iterator)

# 示例一
# 简单的demo：
for i in tqdm(range(100)):
    time.sleep(0.001)
    pass

# 示例二：
# 对于任意list的使用

alist = list('letters')
for letter in tqdm(alist,"Now get ……"):#每次循环都会显示
    time.sleep(0.1)

#观察处理的数据
#通过tqdm提供的set_description方法可以实时查看每次处理的数据
bar = tqdm(["aaaa","bbbb","ccc","ddd"])
for i in bar:
  time.sleep(0.1)
  bar.set_description("Processing %s" %i)
