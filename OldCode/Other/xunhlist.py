class nodeb:
    def __init__(self,s=None):
        self.elm=s
        self.next=None


class linkt:

    def __init__(self):
        self.head=nodeb()
    def insert(self,s):
        if self.head.next==None:
            k = nodeb(s)
            self.head.next=k
        else:
            k=nodeb(s)
            k.next=self.head.next
            self.head.next=k
    def readlink(self):
        if self.head==None:
            return None
        cur=self.head.next


        while cur!=None:

            print (cur.elm)
            cur=cur.next






if __name__ == '__main__':
    l=linkt()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.readlink()
