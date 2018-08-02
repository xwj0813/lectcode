#-*- coding:utf-8 -*-
'''原地删除数组中的重复数字'''

'''不能原地删除重复'''


def removeDuplicates(nums):
    # 原地删除
    #     temp = list(set(nums))
    #     return temp
    newnums = []
    for i in range(len(nums)):
        if nums[i] not in newnums:  # 此时重复了，把该值去除
            newnums.append(nums[i])
    nums = newnums
    print(nums, newnums)
    return len(nums)


def removeDuplicates1(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i = i + 1
            nums[i] = nums[j]
    return i + 1


def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(0, len(nums)):
        if val == nums[j]:
            i = j
            nums[i] = nums[i + 1]
    print(nums)

    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2]
    len = removeElement(nums, 2)
    print(len, nums)
