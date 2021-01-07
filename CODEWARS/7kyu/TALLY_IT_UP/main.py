def score_to_tally(score):
    tally = score
    score_return = 'e <br>'
    counter = 0
    if score == 1:
        return 'a'
    elif score == 2:
        return 'b'
    elif score == 3:
        return 'c'
    elif score == 4:
        return 'd'
    elif score == 5:
        return score_return
    elif score == 10:
        return score_return * 2

    for _ in range(score):
        if 5 > tally >= 0:
            break
        else:

            tally -= 5
            counter += 1
    last_tally = 'a' if tally == 1 else ''
    last_tally = 'b' if tally == 2 else last_tally
    last_tally = 'c' if tally == 3 else last_tally
    last_tally = 'd' if tally == 4 else last_tally
    score_return = score_return * counter + last_tally

    return score_return


print(score_to_tally(15))
