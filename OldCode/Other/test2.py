class Calc(object):
    def __init__(self):
        print ("class init...")
        print('self',self)

    def __new__(cls, *args, **kwargs):
        print("new a class...")
        print(cls)
        return object.__new__(cls)


    def add(self, x, y):
        print (x + y)
    @staticmethod
    def c(x,y):
        print(x*y)
        return x*y
if __name__ == '__main__':
    calc = Calc()
    print (calc)
    calc2=Calc()
    print(calc2)
    print(calc.c(2,9))