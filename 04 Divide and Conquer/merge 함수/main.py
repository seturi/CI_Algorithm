def merge(list1, list2):
    # 코드를 작성하세요.
    combine = []
    list1.sort()
    list2.sort()
    i=0
    j=0
    
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            combine.append(list2[j])
            j += 1
        else:
            combine.append(list1[i])
            i += 1
    if i == len(list1):
        combine += list2[j:]
    else:
        combine += list1[i:]
            
    return combine
    
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))