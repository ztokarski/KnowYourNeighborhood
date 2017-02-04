# import region

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
    sort by item.nazwa
    '''
    return item.nazwa
def getKey2(item):
    '''
    sort by item.typ
    '''
    return item.typ
def getKey3(item):
    '''
    sort by len(item.nazwa)
    '''
    return len(item)
