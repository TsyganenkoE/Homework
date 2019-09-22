import first

def change_flag(number_to_check):
    if number_to_check is -1:
        flg_err = False
    else:
        flg_err = True
    return flg_err

def main_f():
    flg_err = True
    print('First:')
    f_n = first.read_numbers()
    flg_err = change_flag(f_n)
    print('Second:')
    s_n = first.read_numbers()
    flg_err = change_flag(s_n)
    if flg_err is False:
        return
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
