from Task3.Tasks.tasks1.test import print_new_db, tasks1, technic
from Task3.Tasks.tasks2.test import tasks2, list_filenames


def tasks3():
    # tasks3.1
    new_db = tasks1(technic)
    print_new_db(new_db)
    # tasks3.2
    tasks2(list_filenames)


tasks3()
