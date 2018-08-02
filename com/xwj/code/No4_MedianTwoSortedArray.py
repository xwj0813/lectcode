# -*- coding:utf-8 -*-
'''
给出两个有序的数字列表，长度分别为m,n。找到这两个列表中的中间值
'''

import time


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # 创建新列表，并将所有元素初始为0
    nums3 = [0] * (len(nums1) + len(nums2))
    # 指定三个列表的索引，初始值为0
    l_i, r_i, i = 0, 0, 0
    # 当输入两个列表都还存在元素没进行比较的时候，循环进行对比
    # 并将较小值放入新列表，同时较小元素的列表和新列表索引加一
    while(l_i < len(nums1)) and (r_i < len(nums2)):
        if nums1[l_i] < nums2[r_i]:
            nums3[i] = nums1[l_i]
            l_i += 1
        else:
            nums3[i] = nums2[r_i]
            r_i += 1
        i += 1
    # 当存在某一个列表所有元素已经比较完，即拍好了序
    # 剩下那个列表剩下的值直接放入新列表对应位置即可
    if l_i != len(nums1):
        nums3[i:] = nums1[l_i:]
    else:
        nums3[i:] = nums2[r_i:]
    # 小詹有话说：注意‘/’和‘//’的区别 /得到的是float，//得到的是int
    # 前者结果为float类型，后者为整除，结果为int型
    len_3 = len(nums3)
    #‘%’为取模运算，即看长度是否被2整除，即看偶数还是奇数
    if len_3 % 2 != 0:
        return float(nums3[(len_3 - 1) // 2])
    return (nums3[len_3 // 2 - 1] + nums3[len_3 // 2]) / 2


def findMedianSortedArrays_1(nums1, nums2):
    # 简单粗暴将两个列表合成一个
    for i in range(len(nums1)):
        #         if nums1[i] in nums2:
        #             # 如果表1 在表中含有就跳过
        #             continue
        #         else:
        nums2.append(nums1[i])
    # 重新排序
    nums3 = sorted(nums2)
    len_3 = len(nums3)
    if len(nums3) % 2 != 0:  # 奇数
        return float(nums3[(len(nums3) - 1) // 2])
    else:
        return (nums3[len_3 // 2 - 1] + nums3[len_3 // 2]) / 2


if __name__ == '__main__':
    nums1 = [1, 1]
    nums2 = [1, 2]
    start = time.time()
    result = findMedianSortedArrays(nums1, nums2)
    end = time.time()
    print(result, end - start)
    start_1 = time.time()
    result_1 = findMedianSortedArrays_1(nums1, nums2)
    end_1 = time.time()
    print(result_1, end_1 - start_1)
