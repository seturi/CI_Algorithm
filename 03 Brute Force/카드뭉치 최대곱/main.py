def max_product(left_cards, right_cards):
    # 코드를 작성하세요.
    maxvalue = -1
    for lcard in left_cards:
        for rcard in right_cards:
            multi = lcard * rcard
            if multi > maxvalue:
                maxvalue = multi
    return maxvalue
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))