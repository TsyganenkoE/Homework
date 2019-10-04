"""Net delay"""
from sys import stdin
BEGIN = 0
END = 1
TIME = 2
MAX = 10**9
class Net:
    """Net class"""
    def __init__(self, g_array):
        self.array = g_array
    def count_p(self):
        """Count number nodes"""
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
            w_m[gr_edge[BEGIN]][gr_edge[END]] = gr_edge[TIME]
        return w_m

    def the_shortest_way_m(self, node_start, node_end):
        """Matrix of time"""
        way_m = self.make_way_m()
        p_number = self.count_p()
        w_m = [MAX] * (p_number+1)
        w_m[node_start] = 0
        for i in range(p_number+1):
            for j in range(p_number+1):
                if w_m[j] + way_m[j][i] < w_m[i]:
                    w_m[i] = w_m[j] + way_m[j][i]
        return w_m[node_end]

def read_numb():
    """return list consists of lists"""
    array = input()
    res_a = eval(array)
    return res_a

def main_f():
    """read list of nodes, max number of peaks and start_node, find max time"""
    node_arr = read_numb()
    if node_arr == -1:
        print('Incorrect onput')
        return
    max_node = int(input('N:'))
    if max_node > 100:
        return
    start_node = int(input('start node:'))
    if start_node > max_node:
        print(-1)
        return
    net_obj = Net(node_arr)
    max_time = 0
    for j in range(1, max_node+1):
        if j == start_node:
            continue
        delay_time = net_obj.the_shortest_way_m(start_node, j)
        if delay_time > max_time:
            if delay_time != MAX:
                max_time = delay_time
        if (max_time > 6000) | (max_time < 1):
            print(-1)
            return
    print('Net delay:', max_time)
main_f()
