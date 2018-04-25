#!/usr/bin/env python
__author__ = 'Albino'

import random

def distribution(total_money, person_num):
    if total_money < 10:
        return '请包入不低于10元的金额'
    if person_num > 100:
        return '红包个数不能大于100'
    percents = sorted([random.random() for _ in range(person_num - 1)])
    red_envelopes = []
    useless = 0
    for i in range(len(percents)):
        single_red_envelopes = "%.2f"  % (total_money * percents[i] - useless)
        # 处理百分比被占用或者损失精度的情况
        if single_red_envelopes == '0.00' or '-' in single_red_envelopes:
            single_red_envelopes = '0.01'
        red_envelopes.append(single_red_envelopes)
        useless += float(single_red_envelopes)
    red_envelopes.append("%.2f"  % (total_money - useless))
    return red_envelopes

if __name__ == '__main__':
    total_money = int(input('请输入红包总额：'))
    person_num = int(input('请输入红包个数：'))
    red_envelopes = distribution(total_money, person_num)
    if isinstance(red_envelopes, list):
        for red_envelope in red_envelopes:
            print('抢到了{}元'.format(red_envelope))
    else:
        print(red_envelopes)