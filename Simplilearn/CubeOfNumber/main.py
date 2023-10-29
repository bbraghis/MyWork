def cube_printer():
    for i in num:
        cube.append(i ** 3)
    print(cube)


if __name__ == '__main__':
    num = [2, 7, 4, 5, 1, 6]
    cube = []
    cube_printer()
