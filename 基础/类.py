# python中同样使用关键字class创建一个类，类名称第一个字母大写,可以带括号也可以不带括号；
# python中实例化类不需要使用关键字new（也没有这个关键字），类的实例化类似函数调用方式；

#eg:创建一个类，类名称第一个字母大写,可以带括号也可以不带括号

class Student():
    student_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.age = salary
        Student.student_count += 1

    def display_student(self):
        print('Name: {}, age: {}'.format(self.name,self.age))



student1 = Student('cuiyongyuan',10)
student1.display_student()