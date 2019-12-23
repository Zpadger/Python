#定义和使用字典

def main():
    scores = {'张三':95,'李四':78,'王五':82}
    print(scores['张三'])
    print(scores['王五'])
    for elem in scores:
        print('%s\t-->\t%d'%(elem,scores[elem]))
    scores['李四'] = 65
    scores['赵六'] = 71
    scores.update(钱七=67,孙八=85)
    print(scores)

    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('无名氏', 100))
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()