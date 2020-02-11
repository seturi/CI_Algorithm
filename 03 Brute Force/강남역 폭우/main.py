def trapping_rain(buildings):
    # 코드를 작성하세요
    water = 0
    for i in range(1, len(buildings) - 1):
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])
        
        low = min(max_left, max_right)

        water += max(0, low - buildings[i])

    return water

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
