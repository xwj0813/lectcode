# -*- coding:utf-8 -*-
'''三个数之和'''


def threeSum(nums):
    if len(nums) == 0:
        return []
    result = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(i + 2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    print(temp.sort(key=None, reverse=False))
                    if temp not in result and j != k:
                        result.append(temp)
                    temp = []
    print(result)
    return result


'''
1.列表排序，sort()方法
2.一层循环，固定一个数，注意从第二个位置开始要考虑是不是和前一个位置的数值相等，避免做不必要的重复计算，比如代码中举例[-1,-1,0]
3.固定一个数后，另外两个数索引为除去第一个数的首尾位置。
4.取固定数的相反数为目标值target，如果另外两个数之和大于目标值，尾部索引减一，反之首部索引加一
5不大不小即相等，记录这一个解，并首尾索引分别加减一，寻找其他解
'''


def threeSum1(nums):
    res = []
    nums.sort()  # 排序
    print(nums)
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # 收尾
            continue
        target = 0 - nums[i]
        start, end = i + 1, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1  # 大于目标值 尾部索引见一
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                res.append((nums[i], nums[start], nums[end]))
                end -= 1
                start + 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
    return res


'''NO16:找出接近的三个数'''


def threeSumClosest(nums, target):
    res = []
    nums.sort()  # 排序
    print(nums)
    for i, num in enumerate(nums[0:-2]):
        l, r = i + 1, len(nums) - 1
        if num + nums[r] + nums[r - 1] < target:  # 这个是最大值与最小值之和
            res.append(num + nums[r] + nums[r - 1])
        elif num + nums[l] + nums[l + 1] > target:  # 最大值与最小值之间的和
            res.append(num + nums[l] + nums[l + 1])
        else:
            while l < r:
                res.append(num + nums[l] + nums[r])
                if num + nums[l] + nums[r] < target:
                    l += 1
                elif num + nums[l] + nums[r] > target:
                    r -= 1
                else:
                    return target
    # res是一些的数
    print("res", res)
    # 排序找出最接近target的数
    res.sort(key=lambda x: abs(x - target))
    return res[0]


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    result = threeSum1(nums)
    target = 1
    res = threeSumClosest(nums, target)
    print(res)
