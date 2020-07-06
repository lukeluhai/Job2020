class Node:
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_
class Lilo:
    def __init__(self):
        self.head=None
        self.length=0
    def is_empty(self):
        if self.length==0:
            return True
        return False
    def len(self):
        n=0
        if self.head==0:
            return 0
        else:
            p=self.head
            while p.next!=None:
                n+=1
                p=p.next
            return n
    def prepend(self,elem):
        if isinstance(elem,Node):
            p=elem
        else:
            p=Node(elem)
        if self.head==None:
            self.head=p
            self.length+=1
        else:
            pre=self.head
            p.next=pre
            self.head=p
            self.length+=1
    def printLink(self):
        if self.head==None:
            print("None")
        else:
            p=self.head
            while p!=None:
                print(p.elem)
                p=p.next
if __name__ == '__main__':
    linkLilo=Lilo()
    print(linkLilo.is_empty())
    linkLilo.prepend(1)
    linkLilo.prepend(2)
    linkLilo.printLink()

