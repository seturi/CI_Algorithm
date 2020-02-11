def staircase(n):
    # 코드를 작성하세요.
    caselist = [1, 1]
    for i in range(2, n + 1):
        caselist.append(caselist[i - 2] + caselist[i - 1])
    return caselist[n]

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
