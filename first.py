import sys
from sys import stdin
class Node():
    def __init__(self,number=None,next=None):
        self.q=number
        self.next=next

class List():
    def __init__(self):
        self.pointer=None
        self.l=None

    def add_new(self,number):
        tmp=Node()
        tmp.q=number
        tmp.next=None
        if(self.l):
            self.l.next=tmp
            self.l=self.l.next
        else:
            self.pointer=self.l=tmp

    def search(self,elem):
        flg=False
        lst=self.pointer
        if(lst==None):
            print('Empty list')
            return -1
        while(lst!=None):
            if(lst.q==elem):
                flg=True
                break
            else:
                lst=lst.next
        if(flg==True):
            return (lst.q)
        else:
            print('No such elem in list')
            return -1

    def output(self):
        tmp=self.pointer
        if(tmp!=None):
            while(tmp!=None):
                print(tmp.q)
                tmp=tmp.next
            
    def delete_node(self,n):
        cur=prev=self.pointer
        while(cur!=None):
            if(cur.q==n):
                if(cur.next==None):
                        prev.next=None
                        break
                prev.next=cur.next
            prev=cur
            cur=cur.next
            
    def delete(self):
        while(self.pointer!=None):
            lst=self.pointer
            self.pointer=self.pointer.next
            lst=None

    def to_numb(self):
        i=n=0
        tmp=self.pointer
        while(tmp!=None):
            i=(tmp.q*10**n+i)
            n+=1
            tmp=tmp.next
        return i

    def _to_list(self,n):
        while(n>0):
            self.add_new(n%10)
            a=n
            n=(a-n%10)//10

    def __add__(self,obj):
        x=y=0
        x=self.to_numb()
        y=obj.to_numb()
        s=x+y
        Res=List()
        Res._to_list(s)
        return Res

def read_numbers():
    i=flg=True
    n=0
    while i:
        try:
            i=stdin.read(1)
            if(ord(i)==ord('\n')):
                break
            elif((ord(i)>ord('9'))|(ord(i)<ord('0'))):
                print('Not a number')
                flg=False
                break
            else:
                    i=int(i)
                    n=n*10+i
        except EOFError:
            break
    if(flg):
        return n
    else :
        return -1

