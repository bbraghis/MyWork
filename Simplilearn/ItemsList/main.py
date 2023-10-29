def item_list():
    for i in sorted(d.values()):
        print(i)


if __name__ == '__main__':
    d = {'f': 1, 'b': 4, 'a': 3, 'e': 9, 'c': 2}
    item_list()
