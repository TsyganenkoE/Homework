"""Count same substrings in string """
from sys import stdin

def read_str():
    """read strig"""
    main_str = []
    while True:
        try:
            buf_symb = stdin.read(1)
            if buf_symb == '':
                break
            elif ord(buf_symb) is ord('\n'):
                break
            main_str.append(buf_symb)
        except EOFError:
            break
    if not main_str:
        res = -1
    else:
        main_string = "".join(main_str)
        res = main_string
    return res

def main_f():
    """print number of the same substring or error msg if string is incorrect"""
    flg_err = False
    counter_s = 0
    main_string = read_str()
    if main_string == -1:
        return
    sub_str = main_string[counter_s]
    while counter_s is not len(main_string):
        count_sub = main_string.count(sub_str)
        i = count_sub*len(sub_str)
        if i is len(main_string):
            flg_err = True
            break
        counter_s += 1
        sub_str += main_string[counter_s]
    if (flg_err is True)&(count_sub > 1):
        print(str(main_string.count(sub_str)))
    else:
        print('Incorrect string')

main_f()
