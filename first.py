from sys import stdin

class Node():
    def __init__(self, number=None, next_elem=None):
        self.q_n = number
        self.next = next_elem

class List():
    def __init__(self):
        self.pointer = None
        self.last = None

    def add_new(self, new_number):
        tmp = Node()
        tmp.q_n = new_number
        tmp.next = None
        if self.last:
            self.last.next = tmp
            self.last = self.last.next
        else:
            self.pointer = self.last = tmp

    def search(self, elem):
        flg = False
        lst = self.pointer
        if lst is None:
            print('Empty list')
            return -1
        while lst is not None:
            if lst.q_n is elem:
                flg = True
                break
            else:
                lst = lst.next
        if flg is True:
            res_elem = lst.q_n
        else:
            print('No such elem in list')
            return -1
        return res_elem

    def output(self):
        tmp = self.pointer
        if tmp is not None:
            while tmp is not None:
                print(tmp.q_n)
                tmp = tmp.next

    def delete_node(self, number_to_delete):
        cur = prev = self.pointer
        while cur is not None:
            if cur.q_n is number_to_delete:
                if cur.next is None:
                    prev.next = None
                    break
                prev.next = cur.next
            prev = cur
            cur = cur.next

    def delete(self):
        self.pointer = self.last = None

    def to_numb(self):
        i_c = n_c = 0
        tmp = self.pointer
        while tmp is not None:
            i_c = (tmp.q_n*10**n_c+i_c)
            n_c += 1
            tmp = tmp.next
        return i_c

    def to_list(self, numb_to_list):
        while numb_to_list > 0:
            self.add_new(numb_to_list%10)
            numb_to_list = numb_to_list//10

    def __add__(self, obj):
        x_numb = y_numb = 0
        x_numb = self.to_numb()
        y_numb = obj.to_numb()
        sum_n = x_numb+y_numb
        res_list = List()
        res_list.to_list(sum_n)
        return res_list

def read_numbers():
    i_c = flg_err = True
    n_c = 0
    while True:
        try:
            i_c = stdin.read(1)
            if ord(i_c) is ord('\n'):
                break
            elif (ord(i_c) > ord('9')) | (ord(i_c) < ord('0')):
                print('Not a number')
                flg_err = False
                break
            else:
                i_c = int(i_c)
                n_c = n_c * 10+i_c
        except EOFError:
            break
    if flg_err is not True:
        return -1
    return n_c
