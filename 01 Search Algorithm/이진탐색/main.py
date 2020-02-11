def binary_search(element, some_list):
    # 코드를 작성하세요.
    start = 0
    last = len(some_list) - 1
    while start <= last :
        center = (start + last) // 2
        if some_list[center] == element:
            return center
        elif some_list[center] > element:
            last = center - 1
        else:
            start = center + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))