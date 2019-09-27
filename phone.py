"""Phone number"""
from sys import stdin
import itertools

LETTER_ARRAY = [' ', '-', 'abc', 'def', 'ghi',
                'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def read_number():
    """read symb and return phone number or -1 if there were not only numbers"""
    flg_err = True
    ph_number = []
    while True:
        try:
            new_numb = stdin.read(1)
            if new_numb == '':
                break
            elif ord(new_numb) == ord('\n'):
                break
            elif (ord(new_numb) > ord('9')) | (ord(new_numb) < ord('0')):
                flg_err = False
                print('Not a number')
                break
            else:
                ph_number.append(new_numb)
        except EOFError:
            break
    if not ph_number:
        flg_err = False
    if flg_err:
        res = ph_number
    else:
        res = -1
    return res

def find_let(ph_number, numb_counter):
    """make result list that consists of combinations of strings from phone_number"""
    numb_i = int(ph_number[numb_counter])
    new_str = LETTER_ARRAY[numb_i]
    if numb_counter+1 != len(ph_number):
        res_s = map(''.join, itertools.product(new_str, find_let(ph_number, numb_counter+1)))
    else:
        return new_str
    return res_s

def output_result(res_s):
    """print result"""
    res_array = []
    for word in res_s:
        res_array.append(word)
    print(res_array)

def main_f():
    """print letters or error msg if string is not correct"""
    ph_number = read_number()
    if ph_number == -1:
        print('Incorrect number, try again')
        return
    res_l = find_let(ph_number, 0)
    output_result(res_l)
main_f()
