""" The most popular word in text"""
from sys import stdin

def delete_list(list_to_delete):
    """delete list that consists of letters """
    list_len = len(list_to_delete)
    while list_len > 0:
        del list_to_delete[list_len-1]
        list_len -= 1
    return list_to_delete

def read_str():
    """read letters while not eof"""
    new_word = []
    all_words = []
    while True:
        try:
            new_symb = stdin.read(1)
            if new_symb == '':
                break
            elif (ord(new_symb) is ord('\n')) | (ord(new_symb) is ord(' ')):
                if new_word:
                    new_string = ''.join(new_word)
                    new_word = delete_list(new_word)
                    all_words.append(new_string)
            else:
                new_word.append(new_symb)
        except EOFError:
            break
    if not all_words:
        res = -1
    else:
        res = all_words
    return res

def search_the_most_popular_word(all_words, res_list):
    """searches for the max number of occurance of the word in the list of words occurances
    and returns false if there are several words with this number and truth if there is one
    such word """
    max_repeat = max_index = i_index = 0
    flg_err = True
    word = all_words[i_index]
    while i_index != len(all_words):
        if max_repeat == res_list[i_index]:
            if word != all_words[i_index]:
                flg_err = False
        if max_repeat < res_list[i_index]:
            max_repeat = res_list[i_index]
            flg_err = True
            word = all_words[i_index]
            max_index = i_index
        i_index += 1
    return max_index, flg_err

def main_f():
    """print the most popular word in text or -- if there are several popualer words"""
    all_words = read_str()
    res_list = []
    counter = 0
    if all_words == -1:
        return
    while counter != len(all_words):
        res_list.append(all_words.count(all_words[counter]))
        counter += 1
    max_index, flg_err = search_the_most_popular_word(all_words, res_list)
    if flg_err:
        print(all_words[max_index])
    else:
        print('--')

main_f()
