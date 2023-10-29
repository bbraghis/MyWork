def color_items():
    for x in color:
        for y in items:
            print(x, y)
        print('')


if __name__ == '__main__':
    color = ["red", "blue", "white"]
    items = ["apple", "sky", "shirt"]
    color_items()
