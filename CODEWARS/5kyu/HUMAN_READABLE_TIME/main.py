def make_readable(time_in_seconds):
    hours = 0
    minutes = 0
    seconds = time_in_seconds

    for _ in range(time_in_seconds):
        if seconds > 59:
            seconds -= 60
            minutes += 1
            if minutes > 59:
                minutes = 0
                hours += 1
    if hours < 10:
        hours = f'0{str(hours)}'
    if minutes < 10:
        minutes = f'0{str(minutes)}'
    if seconds < 10:
        seconds = f'0{str(seconds)}'

    return '{}:{}:{}'.format(hours, minutes, seconds)


print(make_readable(86400))
