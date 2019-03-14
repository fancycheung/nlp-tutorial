#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: Rank.py
@time: 2019/3/14/上午11:23
@software: PyCharm
"""

"""
排序页面
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def bubbleRank(data):
    """
    冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

    比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    针对所有的元素重复以上的步骤，除了最后一个；
    重复步骤1~3，直到排序完成。

    冒泡排序 时间复杂度 O(n**2), 空间复杂度 O(1), 稳定排序
    :param data:
    :return:
    """
    length = data.__len__()
    for j in range(length - 1):
        for i in range(length - 1 - j):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


def selectorRank(data):
    """
    选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
    然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

    初始状态：无序区为R[1..n]，有序区为空；
    第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。
    该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，
    使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
    n-1趟结束，数组有序化了。

    选择排序 时间复杂度 O(n**2), 空间复杂度 O(1), 不稳定排序
    :param data:
    :return:
    """
    length = data.__len__()
    for i in range(length - 1):
        index = i
        for j in range(i, length):
            if data[j] < data[index]:
                index = j
        data[i], data[index] = data[index], data[i]
    return data


def insertRank(data):
    """
    插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。
    它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

    从第一个元素开始，该元素可以认为已经被排序；
    取出下一个元素，在已经排序的元素序列中从后向前扫描；
    如果该元素（已排序）大于新元素，将该元素移到下一位置；
    重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    将新元素插入到该位置后；
    重复步骤2~5。

    插入排序 时间复杂度 O(n**2), 空间复杂度 O(1), 稳定排序
    :param data:
    :return:
    """
    length = data.__len__()
    for i in range(1, length):
        index = i - 1
        current = data[i]
        while index >= 0 and current < data[index]:
            data[index + 1] = data[index]
            index -= 1
        data[index + 1] = current
    return data


def shellRank(data):
    """
    第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，
    它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

    选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
    按增量序列个数k，对序列进行k 趟排序；
    每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，
    分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

    希尔排序 时间复杂度 O(n**1.3), 空间复杂度 O(1), 不稳定排序
    :param data:
    :return:
    """
    length = data.__len__()
    gap = length/2
    while gap > 0:
        for i in range(gap, length):
            j = i
            current = data[i]
            while j - gap > 0 and current < data[j - gap]:
                data[j] = data[j - gap]
                j -= gap
            data[j] = current
        gap = gap/2
    return data


if __name__ == "__main__":
    data = [1,3,4,2,8,6,5,3]
    # print bubbleRank(data)
    # print selectorRank(data)
    # print insertRank(data)
    print shellRank(data)
    pass
