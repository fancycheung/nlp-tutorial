#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: BubbleRank.py
@time: 2019/3/14/上午11:23
@software: PyCharm
"""

"""
冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

比较相邻的元素。如果第一个比第二个大，就交换它们两个；
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。 

冒泡排序 时间复杂度 O(n*n), 空间复杂度 O(1), 稳定排序
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def rank(data):
    """
    对于列表排序
    :param data:
    :return:
    """
    length = data.__len__()
    for j in range(length - 1):
        for i in range(length - 1 - j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


if __name__ == "__main__":
    data = [1,3,4,2,8,6,5,3]
    print rank(data)
    pass
