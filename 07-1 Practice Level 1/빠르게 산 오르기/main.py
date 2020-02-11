def select_stops(water_stops, capacity):
    # 코드를 작성하세요. 
    list = []
    curr_water = capacity
    
    for i in range(len(water_stops)-1):
        if i == 0:
            curr_water -= water_stops[0]
        else:
            curr_water -= (water_stops[i] - water_stops[i-1])
        
        if curr_water < (water_stops[i+1] - water_stops[i]):
            curr_water = capacity
            list.append(water_stops[i])
    
    list.append(water_stops[-1])
    
    return list

# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))