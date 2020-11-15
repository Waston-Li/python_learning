#dict() 函数用于创建一个字典。
dict()                        # 创建空字典
dict(a='a', b='b', t='t')     # 传入关键字
dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
dict([('one', 1), ('two', 2), ('three', 3)])

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#enumerate(sequence, [start=0]) 返回 enumerate(枚举) 对象。
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
list(enumerate(seasons, start=1))
#for循环使用enumerate
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print (i, element)