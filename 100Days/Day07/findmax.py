#找出列表中最大或最小的元素

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)
    # if max_value in fruits:
    #     fruits.remove(max_value)
    # max_value = min_value = fruits[0]
    # for index in range(1, len(fruits)):
    #     if fruits[index] > max_value:
    #         max_value = fruits[index]
    #     elif fruits[index] < min_value:
    #         min_value = fruits[index]
    # print('Second_Max:', max_value)


if __name__ == '__main__':
    main()
# 想一想如果最大的元素有两个要找出第二大的又该怎么做
# 思路：用remove或者discard方法，去掉最大值，然后再重复一次操作，得到第二大的元素