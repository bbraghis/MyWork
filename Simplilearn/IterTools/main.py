def iter_tool():
    from itertools import zip_longest
    first = ['Lionel', 'Cristiano', 'Mohamed', 'Lionel', 'Cristiano', 'Mohamed']
    last = ['Messi', 'Ronaldo', 'Salah']
    for i in zip_longest(first, last, fillvalue='Not defined'):
        print(i)


if __name__ == '__main__':
    iter_tool()
