# 顺序查找

def seq_search(items, key):

    for index, item in enumerate(items):
        if item == key:
            return index
    return -1