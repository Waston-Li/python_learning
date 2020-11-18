# 1Ctrl + Enter：在下方新建行但不移动光标；
#
# 2、Shift + Enter：在下方新建行并移到新行行首；
#
# 选择的行；
#

# 斐波那契数列
from tqdm import tqdm

a,b=0,1
while b<20:
    print(b,end='->')
    a,b=b,a+b #注意这种一行写多个赋值的方法
print()

# age=int(input('输入你的年龄:'))
# print(age)
print('以下while循环内容：\n')
# python的while循环
n=100;sum=0;c=1
while c<=n:
    sum+=c
    c+=1
print("1- %d 的和：%d "%(n,sum)) #注意%的用法
print(r'字符串前面加一个r表示不会发生\的转译\n')

c=0
while c<5:
    print(c,end='')
    c+=1
else:
    print('结束while的条件语句，并执行',c)     #python中的while-else语句当条件语句为fale时执行else;for-else同理

# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
print('以下for循环内容：\n')
languages=['C','C++','Python',2,'Java']
for i in tqdm(languages):
    if(i==2):
        break
    else:
        print('循环中',i)
else:
    print('执行完for循环\n')  #从beak/continue跳出，不执行else

#range()函数完成数字序列的 遍历
for i in range(3):
    print(i,end='')
else:
    print()

for i in range(3,5):    #range()也可以指定区间,注意右区间'达不到'
    print(i,end='')
else:
    print()

for i in range(5,11,2): #range()可以设定增量,注意右区间'达不到'；负增量和区间也可以
    print(i, end='')
else:
    print()


IT = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(IT)):               #结合range()和len()函数以遍历一个序列的索引,len()计算列表的长度
    print(i,'-',IT[i],end=' ')
    pass  #pass用作占位语句

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
#函数部分
print('\n以下是函数部分：')
# 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，传入无法改变，（本身就属于不可变对象）没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
# 可变类型：类似 c++ 的引用传递，如列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

def pif1(name='Waston',age=23): #默认参数
    print(name,'\n',age,'\n')
pif1()

def pif2(a1,*var): # 不定长参数前面带*，会以元组的形式导入
    print(a1);        print('不定长变量组：',var);print()
pif2(1,2,3,'元组形式',4)

def pif3(**var):  # **的参数会以字典形式导入
    print(var)
pif3(dada=1,b=2,c='da')

dic={'d':1,123:'da'}   #注意导入与创建字典形式的区分

# 如果单独出现星号 * 后的参数必须用关键字传入
def pif4(a,*,b):
    return a+b

print(pif4(1,b=2))
#匿名函数lambda
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# lambda [arg1 [,arg2,.....argn]]:expression
sum1=lambda a,b:a+b
print(sum1(999,1))
