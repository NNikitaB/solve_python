from Task3.Tasks.tasks1.test import print_new_db, tasks1, technic
from Task3.Tasks.tasks2.test import tasks2, list_filenames


def tasks3():
    """
    Применяет функции с задачами 3.1 и 3.2
    :return:
    """
    # tasks3.1
    new_db = tasks1(technic)
    print_new_db(new_db)
    # tasks3.2
    new_ls = tasks2(list_filenames)
    print(new_ls)


tasks3()
