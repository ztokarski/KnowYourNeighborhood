
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
    print('''
\033[1;37;49m
            .          .          .
            ■■■■■■     ■■■■■■     ■■■■■■
            \033[1;31;49m■■■■■■     ■■■■■■     ■■■■■■
            \033[0;37;49m|          |          |''')


def get_shapes_table(self):
    '''
    This method display shapes list in table.
    '''
    print("\n")
    '''
    header
    '''
    title_list = ["name", "amount"]
    table = []
    for obj in self.shapes:
        line_lst = [str(self.shapes.index(obj)+1), obj.__class__.__name__, str(obj), "%.2f" % float(obj.get_perimeter()), str(
            obj.get_perimeter_formula()), "%.2f" % float(obj.get_area()), str(obj.get_area_formula())]
        table.append(line_lst)
    table.insert(0, title_list)
    width_list = []
    for i in range(len(table[0])):
        longest_string = 0
        for row in table:
            if len(row[i]) > longest_string:
                longest_string = len(row[i])
        width_list.append(longest_string)

    print("*", end="")
    for column in range(len(table[0])):
        print("{0:-^{w}}".format("-", w=width_list[column] + 2), end="")
        if column + 1 != len(table[0]):
            print("-", end="")
    print("*\n", end="")
    '''
    content
    '''
    for row_number, row in enumerate(table):
        for column, cell in enumerate(row):
            print("|{0:^{w}}".format(cell, w=width_list[column] + 2), end="")
        print("|\n", end="")
        if row_number + 1 != len(table):
            print("|", end="")
            for column, cell in enumerate(row):
                print("{0:═^{w}}".format("═", w=width_list[column] + 2), end="")
                if column + 1 != len(table[0]):
                    print("|", end="")
            print("|\n", end="")
        '''
        footer
        '''
        if row_number + 1 == len(table):
            print("*", end="")
            for column, cell in enumerate(row):
                print("{0:-^{w}}".format("-", w=width_list[column] + 2), end="")
                if column + 1 != len(table[0]):
                    print("-", end="")
            print("*")
    table.remove(table[0])
    return str()
