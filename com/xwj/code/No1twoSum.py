#-*-coding:utf-8 -*-
'''打卡
给出一个数字列表和一个目标值（target），假设列表中有且仅有两个数相加等于目标值，
我们要做的就是找到这两个数，并返回他们的索引值。
'''
import time
# 思路一，两层循环


def twoSum(nums, target):
    """
    :nums 列表
    :target 目标值
    """
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result

# 思路二：有且仅有一个解，可以通过target与某一个元素的差值是否在列表中


def twoSum_1(nums, target):
    '''
    :nums 列表值
    :target 目标值 
    '''
    result = []
    for i in range(len(nums)):
        oneNum = nums[i]
        twoNum = target - nums[i]
        if twoNum in range(len(nums)):
            j = nums.index(twoNum)
            if i != j:
                result.append(i)
                result.append(j)
                return result
# 思路三：通过创建字典，将nums里的值和序号对应起来，并创建另一个字典存储目标值-nums的值，通过
# 过判断该值是否在nums内进行判断并返回其对应的索引


def twoSum_2(nums, target):
    """
    :nums 列表
    :target 目标值
    """
    # 创建字典一，存储输入的列表的元素值和对应的索引
    num_dict = {nums[i]: i for i in range(len(nums))}
    print(num_dict)
    # 创建另一个字典，存储target-列表中的值，
    num_dict2 = {i: target - nums[i] for i in range(len(nums))}
    print(num_dict2)
    # 判断
    result = []
    for i in range(len(nums)):
        j = num_dict.get(num_dict2.get(i))
        if (j is not None) and (j != i):
            result = [i, j]
            break
    return result


def twoSum_3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    dd = {nums[i]: i for i in range(n)}
    for i in range(n - 1):
        cha = target - nums[i]
        if cha in dd and i != dd[cha]:
            return [i, dd[cha]]
    return 'null'


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    start = time.time()
    result = twoSum(nums, target)
    end = time.time()
    print(result, end - start)
    # \
    start = time.time()
    result = twoSum_1(nums, target)
    end = time.time()
    print(result, end - start)
    ###############################
    start = time.time()
    result = twoSum_2(nums, target)
    end = time.time()
    print(result, end - start)
    ##################################
    start = time.time()
    result = twoSum_3(nums, target)
    end = time.time()
    print(result, end - start)
