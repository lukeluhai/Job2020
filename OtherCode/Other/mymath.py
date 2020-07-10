
def getmoney(years, rates):
    return(((1 + rates)**(years + 1) - 1)/(rates))


if __name__ == '__main__':
    print(getmoney(10, 0.03))

from random import randint
data=[randint(-10,10) for x in range(20)]
print (data)

