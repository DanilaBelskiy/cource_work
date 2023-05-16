def check_half(array, start, end, to_find):

    #print(start, end)

    if end - start < 2:
        return -1

    elif array[(start+end)//2] == to_find:
        return (start+end)//2

    elif array[(start+end)//2] < to_find:
        return check_half(array, (start+end)//2, end, to_find)

    elif array[(start+end)//2] > to_find:
        return check_half(array, start, (start+end)//2, to_find)


def binary_search(array, to_find):

    return check_half(array, 0, len(array)-1, to_find)