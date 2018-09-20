
def sum_of(_list):
    result = 0
    for item in _list:
        result += item
    return result

def largest_of(_list):
    _list.sort()
    return _list[-1]

def smallest_of(_list):
    _list.sort()
    return _list[0]

def even_of(_list):
    new_list = []
    for item in _list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

def pos_of(_list):
    new_list = []
    for item in _list:
        if item > 0:
            new_list.append(item)
    return new_list

def mult_all(_list,factor):
    new_list = []
    for item in _list:
        new_list.append(item * factor)
    return new_list

def vector_mult(_list,factor_list):
    new_list = []
    index = 0
    for item in _list:
        new_list.append(item * factor_list[index])
        index += 1
    return new_list

def add_matrices(_list1,_list2):
    xlen = len(_list1[0])
    ylen = len(_list1)
    new_list = []
    for i in range(ylen):
        new_list.append([])
        for n in range(xlen):
            new_list[i].append(_list1[i][n] + _list2[i][n])
    return new_list

def de_dup(_list):
    index = 0
    new_list = []
    for item in _list:
        if item in _list[:index]:
            continue
        else:
            new_list.append(item)
        index += 1
    return new_list

def mult_matrices(_list1,_list2):
    xlen1 = len(_list1[0])
    ylen1 = len(_list1)
    xlen2 = len(_list2[0])
    ylen2 = len(_list2)
    
    new_list = []
    for n in range(ylen1):
        new_list.append([])

    for yi1 in range(ylen1):
        for xi2 in range(xlen2):
            result = 0
            for yi2 in range(ylen2):
                result += _list2[yi2][xi2] * _list1[yi1][yi2]
            new_list[yi1].append(result)

    return new_list
