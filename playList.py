lis1=['hello List']
print(lis1[0].title()) #.title()使首字母大写
#修改添加删除元素
lis1[0]='修改成功'; print(lis1)

lis1.append('.append()在列表末尾添加新元素'); print(lis1)
lis1+=['末尾元素'] #+=添加元素,或拼接列表

del lis1[0]; print("使用del删除元素")
print("使用.pop()弹出列表末尾最后一个元素，之后删除这个元素:"+lis1.pop())
#.pop()可以也删除列表中的任何位置的元素，只需在括号中指定索引即可

#根据值删除元素.remove()
moto_car=['ducati','yamaha','suziki']
too_expensive='ducati' ; moto_car.remove(too_expensive) #也可以写为moto.remove('ducati')

#组织列表
print('sorted()使表中元素按字母顺序排列:',end=""); print(sorted(moto_car))
# .sort()  此方法修改表内元素顺序 ，若想不修改的按顺序输出可以使用 sorted(x)
# .sort(reverse=True)可以按字母反序排列表中的元素
print("len()返回列表长度："+str(len(moto_car)))
#测试pycharm中的git