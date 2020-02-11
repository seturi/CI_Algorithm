def trapping_rain(buildings):
    # 코드를 작성하세요

    water = 0
    n = len(buildings)

    left_list = [0] * n
    right_list = [0] * n
    
    left_list[0] = buildings[0]
    for i in range(1, n):
        left_list[i] = max(left_list[i - 1], buildings[i])
                
    right_list[-1] = buildings[-1]
    for i in range(n - 2, -1, -1):
        right_list[i] = max(right_list[i + 1], buildings[i])    
    
    for i in range(n):
        low = min(left_list[i], right_list[i])
        water += max(0, low - buildings[i])

    return water

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))