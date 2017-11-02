# -*- coding:utf-8 -*-


from generate_random_demo import generate_random


def generate_idno():
    birth_day = raw_input(u'请输入出生日期，格式为 yyyymmdd：')
    idno = generate_random(6) + str(birth_day) + generate_random(3)
    return idno