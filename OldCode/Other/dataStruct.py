
class node:
    pass
    def __init__(self,data):
        self.data=data
        self.next=None
class linkTable:
    def __init__(self):
        self.head=None
    def appendAtStart(self,data):
        p=node(data)
        p.next=self.head
        self.head=p
    def __len__(self):
        lcount=0
        p=self.head
        while p!=None:
            lcount+=1
            p=p.next
        return lcount
    def appendAtEnd(self,data):
        p=node(data)
        q=self.head
        if q==None:
            p.next=self.head
            self.next=p
        else:
            while q.next!=None:
                q=q.next
            q.next=p

    def travel(self):
        if self.head!=None:
            p=self.head
            while p!=None:
                print(p.data)
                p=p.next
        else:
            print("this linkTable is Null")
    def insert(self,pos,data):
        p=node(data)
        count=1
        if pos>self.__len__():
            pos=self.__len__()
        q=self.head
        if q==None:
            self.appendAtEnd(data)
        else:
            while q!=None and count<=pos-1:
                if count==pos-1:
                    p.next=q.next
                    q.next=p
                q=q.next
                count+=1



if __name__ == '__main__':
    lt=linkTable()
    for i in range(10):
        lt.appendAtStart(1)
    for i in range(10):
        lt.appendAtEnd(1)
    lt.insert(6,10)
    lt.travel()
    print(lt.__len__())
