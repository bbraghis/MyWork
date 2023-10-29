def zip_function():
    first = ['Lionel', 'Cristiano', 'Mohamed']
    last = ['Messi', 'Ronaldo', 'Salah']
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in zip(first, last, num):
        print(i)


if __name__ == '__main__':
    zip_function()
