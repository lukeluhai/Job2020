import multiprocessing
import time
import threading


def printa():
    for i in range(10):
        time.sleep(0.01)
        print("a_"+str(i))


def printb():
    for i in range(10):
        time.sleep(0.01)
        print("b_"+str(i))

def printt1():
    for i in range(10):
        time.sleep(0.01)
        print("t1_"+str(i))


def printt2():
    for i in range(10):
        time.sleep(0.01)
        print("t2_"+str(i))
if __name__ == "__main__":
    print('start')
    a=multiprocessing.Process(target=printa)
    b=multiprocessing.Process(target=printb)
    a.start()
    b.start()


    t1 = threading.Thread(target=printt1)
    t2 = threading.Thread(target=printt2)
    t1.start()
    t2.start()
    print('end')