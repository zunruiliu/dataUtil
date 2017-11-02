# -*- coding:utf-8 -*-

from random import randint
from random import choice


def generate_cardNo():
    card_header_tmp = ['622700', '621488']
    card_header = choice(card_header_tmp)
    res_tmp = ''
    if card_header is '622700':
        for i in range(0, 8):
            res_tmp = res_tmp + str(randint(0, 9))
            res = '99211' + res_tmp
    elif card_header is '621488':
        for i in range(0, 10):
            res_tmp = res_tmp + str(randint(0, 9))
            res = res_tmp
    return card_header + res


if __name__ == '__main__':
    print generate_cardNo()