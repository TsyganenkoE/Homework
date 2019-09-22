import first

def main_f():
    print('First:')
    f_n = first.read_numbers()
    print('Second:')
    s_n = first.read_numbers()
    first_list = first.List()
    first_list.to_list(f_n)
    second_list = first.List()
    second_list.to_list(s_n)
    res_list = first.List()
    res_list = first_list+second_list
    print('Result:')
    res_list.output()
    first_list.delete()
    second_list.delete()
    res_list.delete()

main_f()
