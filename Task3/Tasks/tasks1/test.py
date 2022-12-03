
# БД
technic = [
    ('Ноутбук', 1500, 'Татьяна', '89002001020'),
    ('Смартфон', 500, 'Анна', '89202202325'),
    ('Проектор ', 300, 'Андрей', '89505205656'),
    ('Принтер', 750, 'Игорь', '89303303236'),
    ('Планшет', 2300, 'Игорь', '89303303236'),
    ('Смартфон', 1000, 'Андрей', '89505205656'),
    ('Ноутбук', 4800, 'Татьяна', '89002001020'),
    ('Наушники', 780, 'Марина', '89562002350'),
    ('Сканер', 550, 'Сергей', '89808564559'),
    ('Планшет', 1200, 'Анна', '89202202325'),
    ('Ноутбук', 1100, 'Игорь', '89303303236'),
    ('Смартфон', 3500, 'Татьяна', '89002001020')
]


# Поиск пары в массиве пар,возврат -1, если не нашли
def _search(arr, name, number):
    for count, value in enumerate(arr):
        if value[0] == name and value[1] == number:
            return count
    return -1


def tasks1(db):
    """
    Оптимизация хранения в БД
    :param db: database
    :return : new_db
    """
    new_db = []
    for it in db:
        number = _search(new_db, it[2], it[3])
        if number == -1:
            new_db.append((it[2], it[3], [(it[0], it[1])]))
        else:
            new_db[number][2].append((it[0], it[1]))
    return new_db


def print_new_db(new_db):
    """
    Вывод БД
    :param new_db:
    :return:
    """
    for it in new_db:
        s = '{0} {1}:'.format(it[0], it[1])
        ls = []
        for i in it[2]:
            ls.append(' {0} - {1}'.format(i[0], i[1]))
        s += ';'.join(ls)
        print(s)
