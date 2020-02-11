def sublist_max(profits):
    # 코드를 작성하세요. 
    max_profit = profits[0]
    for i in range(len(profits)):
        curr_profit = 0
        for j in range(i, len(profits)):
            curr_profit += profits[j]
            if curr_profit > max_profit:
                max_profit = curr_profit
    return max_profit


# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))