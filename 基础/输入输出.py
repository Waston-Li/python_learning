# 将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
x = 10 * 3.25
y = 200 * 200 #此时为数字型
s = 'NO!x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...' #repr()/str()转换字符串函数
print(s[3:])     # repr() 內的参数可以是 Python 的任何对象

# str.rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。还有类似的方法, 如 ljust() 和 center()。
# .zfill(n), n个位置它会在字符剩余位置的左边填0

for x in range(1,5):   #打印平方和立方表
    print(str(x).rjust(2),repr(x**2).rjust(3),repr(x**3).rjust(4))#注意用repr转为字符型才可用此函数

print('\n以下是format的测试：')
# str.format()括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在formart中的位置
print('{1} {0}'.format('语言',"python"))
print('{IT} 流批 '.format(IT='python')) #在format使用了关键字，值会指向该参数/可以与位置结合
# !a()使用ascii(），!s / !r用str()和repr()在可以对其进行转化
import math
print('{!r}'.format(math.pi))

#    : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
print('pi{0:6.3f}以及域宽写法{1:5d}'.format(math.pi,33)) #d后缀代表整数，f小数如6.3f表示6域宽保留3位小数
                                              # 其余为字符型
for i in range(1,4):
    for j in range(1,4):
        print('{0:3d}'.format(i),end='')
    print()
print('pi的值位%6.3f'%math.pi)
# 因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。
# 但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().

#文件的写入
print('{}'.format('\n以下是文件的内容：'))
# open() 将会返回一个 file 对象，基本语法格式如:open(filename, mode)
f=open("/Users/Mr_QL/Documents/python_学习/python基础/ex.txt","w") #路径，打开模式
f.write('Python是一个很好的语言\n 非常好')
f.close()
#更多文件操作：参考https://www.runoob.com/python3/python3-inputoutput.html
# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

