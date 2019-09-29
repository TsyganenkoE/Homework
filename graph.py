"""Graph"""
from sys import stdin

BEGIN = 0
END = 1
class Graph:
    """Graph class that has edge field and methods that realises DFS and BFS algs"""
    def __init__(self, g_array):
        self.array = g_array

    def d_f_s(self, cur_p, prev_p, visited_p):
        """DFS algorithm """
        graph_a = self.array
        p_arr = []
        for gr_edge in graph_a:
            if (gr_edge[BEGIN] == cur_p) & (gr_edge[END] != prev_p):
                p_arr.append(gr_edge[END])
            elif (gr_edge[END] == cur_p) & (gr_edge[BEGIN] != prev_p):
                p_arr.append(gr_edge[BEGIN])
        if not p_arr:
            visited_p.append(prev_p)
            return
        for i in p_arr:
            if i == cur_p:
                continue
            visited_p.append(i)
            self.d_f_s(i, cur_p, visited_p)
        visited_p.append(prev_p)

    def b_f_s(self, cur_p, prev_p, visited_l, q_p):
        """BFS algorithm """
        graph_a = self.array
        p_arr = []
        if cur_p in visited_l:
            return
        visited_l.append(cur_p)
        for gr_edge in graph_a:
            if (gr_edge[BEGIN] == cur_p) & (gr_edge[END] != prev_p):
                p_arr.append(gr_edge[END])
            elif (gr_edge[END] == cur_p) & (gr_edge[BEGIN] != prev_p):
                p_arr.append(gr_edge[BEGIN])
        for i in p_arr:
            if i not in visited_l:
                q_p.append(i)
        while q_p:
            self.b_f_s(q_p.pop(0), cur_p, visited_l, q_p)

def read_numb():
    """returns list consists of lists"""
    begin = end = number = 0
    array = []
    full_array = []
    flg_err = True
    while True:
        try:
            symb = stdin.read(1)
            if symb == '':
                break
            elif ord(symb) == ord(' '):
                begin = number
                array.append(begin)
                number = 0
            elif ord(symb) == ord('\n'):
                end = number
                array.append(end)
                number = 0
                full_array.append(array.copy())
                array.clear()
            elif (ord(symb) > ord('9'))|(ord(symb) < ord('0')):
                flg_err = False
                break
            else:
                number = number*10+int(symb)
        except EOFError:
            break
    if flg_err is False:
        res_a = -1
    else:
        res_a = full_array
    return res_a

def main_f():
    """make graph object and applies DFS and BFS algorithms to it"""
    gr_array = read_numb()
    if gr_array == -1:
        print('Incorrect input')
        return
    graph_obj = Graph(gr_array)
    start = 0
    visited_p = [start]
    graph_obj.d_f_s(start, start, visited_p)
    visited_p.pop()
    print('DFS:', visited_p)
    visited_l = []
    q_p = []
    graph_obj.b_f_s(start, start, visited_l, q_p)
    print('BFS:', visited_l)

main_f()
