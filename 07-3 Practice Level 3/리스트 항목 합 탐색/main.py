def sum_in_list(search_sum, sorted_list):
    # 코드를 쓰세요
    """
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] + sorted_list[j] == search_sum:
                return True
    return False
    """
    
    for i in sorted_list:
        if (search_sum - i) in sorted_list:
            return True
    return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))