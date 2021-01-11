def solution(n):
    while n == 4:
        n += 3
        return n

    while n == 7:
        n -= 3
        return n

    while n != 4 or n != 7:
        return False


print(solution(4))
