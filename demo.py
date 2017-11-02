# -*- coding:utf-8 -*-

from base.generate_idno_demo import generate_idno


def check_bit(idno):
    res = 0
    iW = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    last_bit = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    for i in range(0, len(idno)):
        res = res + int(idno[i]) * iW[i]

    check_right_bit = last_bit[res % 11]
    return idno + check_right_bit

if __name__ == '__main__':
    print check_bit(idno=generate_idno())