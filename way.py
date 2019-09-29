"""The shotrest way"""
from sys import stdin
BEGIN = 0
END = 1
WEIGHT = 2
MAX = 10**9
class Graph:
    """Graph class"""
    def __init__(self, g_array):
        self.array = g_array
    def count_p(self):
        """Count number peaks"""
        graph_a = self.array
        max_p = -1
        for i in graph_a:
            if i[BEGIN] > max_p:
                max_p = i[BEGIN]
            elif i[END] > max_p:
                max_p = i[END]
        return max_p

    def make_way_m(self):
        """Matrix"""
        graph_a = self.array
        p_number = self.count_p()
        w_m = [[MAX for i_counter in range(p_number+1)] for i_counter in range(p_number+1)]
        for gr_edge in graph_a:
            w_m[gr_edge[BEGIN]][gr_edge[END]] = gr_edge[WEIGHT]
        for gr_edge in graph_a:
            w_m[gr_edge[END]][gr_edge[BEGIN]] = gr_edge[WEIGHT]
        return w_m

    def the_shortest_way_m(self, node_start):
        """Matrix of weigths"""
        way_m = self.make_way_m()
        p_number = self.count_p()
        w_m = [MAX] * (p_number+1)
        w_m[node_start] = 0
        prev = [-1]*(p_number+1)
        prev[node_start] = 0
        for i in range(p_number+1):
            for j in range(p_number+1):
                if w_m[j] + way_m[j][i] < w_m[i]:
                    w_m[i] = w_m[j] + way_m[j][i]
                    prev[i] = j
        return w_m, prev

    def result(self, node_start, node_end):
        """Print the shortest way"""
        weight_m, prev = self.the_shortest_way_m(node_start)
        j = node_end
        way_a = []
        while j != node_start:
            if j!=-1:
                way_a.append(j)
            j = prev[j]
        way_a.append(j)
        print('She shortest way is :', way_a[::-1])

def read_numb():
    """return list consists of lists"""
    begin = number = weight = 0
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
                weight = number
                array.append(weight)
                number = 0
                full_array.append(array.copy())
                array.clear()
            elif (ord(symb) > ord('9')) | (ord(symb) < ord('0')):
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
    """main read graph read start and ends point then print the way"""
    gr_array = read_numb()
    if gr_array == -1:
        print('Incorrect input')
        return
    graph_obj = Graph(gr_array)
    start = int(input('Start:'))
    end = int(input('End:'))
    graph_obj.result(start, end)
main_f()
