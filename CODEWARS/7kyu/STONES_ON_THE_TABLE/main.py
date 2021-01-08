def solution(stones):
    stones_needed_to_be_removed = 0
    stones = list(stones)
    for index in range(len(stones)):
        try:
            if stones[index] == stones[index + 1]:
                stones_needed_to_be_removed += 1
        except IndexError:
            pass
    return stones_needed_to_be_removed


print(solution('RGGBB'))
