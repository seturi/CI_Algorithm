def fib_optimized(n):
    # 코드를 작성하세요.
    prev = 0
    curr = 1
    i = 1
    while i < n:
        fib = prev + curr
        prev = curr
        curr = fib
        i += 1
    return curr
    


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
