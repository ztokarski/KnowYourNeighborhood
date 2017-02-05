
def open_data(file_name):
    '''
    open csv file and returns list of lists without headline (first line)
    '''
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split("\t") for element in lines]
    return table[1:]


def getKey(item):
    '''
    sort by name of object (item.nazwa)
    '''
    return item.nazwa


def getKey2(item):
    '''
    sort by type of object (item.typ)
    '''
    return item.typ


def getKey3(item):
    '''
    sort by length of name (item.nazwa)
    '''
    return len(item)


def flag():
    '''
    pictrure of the Polish flag
    '''
    print('''
                \033[1;37;49m
                .          .          .
                ■■■■■■     ■■■■■■     ■■■■■■
                \033[1;31;49m■■■■■■     ■■■■■■     ■■■■■■
                \033[0;37;49m|          |          |''')
