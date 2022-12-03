
# Список имен файлов
list_filenames = [
    'filename1',
    'filename1ddhykiukui',
    'filename',
    'filename1123456789',
    'filename10',
    'fname2',
    'filename10'
]


# Удаление дубликатов символов
def del_duplicate_char(strings):
    arr = []
    for string in strings:
        old_string = string
        new_string = old_string[0]
        for char in old_string[1:]:
            if char != new_string[-1]:
                new_string += char
        arr.append(new_string)
    return arr


def tasks2(ls_filenames):
    """
    Дополняет имена файлов '_' до наибольшей длинны
    и удаляет дубликаты символов
    :param ls_filenames:
    :return:new_ls
    """
    max_len = max(map(len, ls_filenames))
    ls_filenames = del_duplicate_char(ls_filenames)
    new_ls = list(map(lambda st: st+'_'*(max_len-len(st)) if len(st) < max_len else st, ls_filenames) )
    return new_ls



