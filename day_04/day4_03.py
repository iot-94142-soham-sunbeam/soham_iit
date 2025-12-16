def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
def overlapping(list1, list2):
    return bool(set(list1) & set(list2))
