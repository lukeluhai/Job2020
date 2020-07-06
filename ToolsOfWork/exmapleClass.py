class exmapleClass:
    # 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用self.classCount,exmapleClass.classCount
    __counts = 0  # 私有变量
    classCount = 0 # 公开变量
    def __init__(self,a1,b1):
        self.a1 = a1
        self.b1 = b1
        exmapleClass.classCount += 1
    def printa1(self):
        print(self.a1)
    def __ss(self):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    # __dict__: 类的属性（包含一个字典，由类的数据属性组成）
    # __doc__: 类的文档字符串
    # __name__: 类名
    # __module__: 类定义所在的模块（类的全名是
    #'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__等于mymod）
    # __bases__: 类的所有父类构成元素（包含了一个由所有父类组成的元组）
    def __del__(self):
        print('销毁')
'''
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *

__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
'''
a = exmapleClass(1,2)
b = exmapleClass(11,22)
print(exmapleClass.classCount)
print(a.__dict__)
print(a.__doc__)
print(a.__class__)
print(a.__module__)
    

#print(a.__name__)
#print(a.__base__)
print('hello world')

class ChildExmapleClass(exmapleClass):
    def __init__(self,a1,b1,c1):
        super(ChildExmapleClass,self).__init__(a1,b1)
        self.c1=c1
    def printc1(self):
        print(self.c1)

c = ChildExmapleClass(111,222,333)
c.printa1()
c.printc1()
print(ChildExmapleClass.classCount)

print(issubclass(ChildExmapleClass,exmapleClass))
print(isinstance(a,exmapleClass))
print(a.__str__()) # 用于将值转化为适于人阅读的形式
print(a.__repr__()) #转化为供解释器读取的形式
# print(a.__cmp__(b)) #对象比较