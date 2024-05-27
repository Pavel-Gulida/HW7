
def common_elements():
    list1 = set(range(0,100, 3))
    list2 = set(range(0,100, 5))
    list3 = list1.intersection(list2)
    return list3

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")