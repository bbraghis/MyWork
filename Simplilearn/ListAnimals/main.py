def animal_list():
    animals = [{"name": "Dogs", "age": 11}, {"name": "Lion", "age": 30},
               {"name": "Elephant", "age": 63}, {"name": "Leopard", "age": 18}]
    for animals in filter(lambda i: i["age"] % 2 == 0, animals):
        print(animals)


if __name__ == '__main__':
    animal_list()
