class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

        if self.second > 59:
            self.minute += 1
            self.second -= 60

        if self.minute > 59:
            self.hour += 1
            self.minute -= 60

        if self.hour > 23:
            self.hour -= 24

    def __str__(self):
        return f'{self.hour}:{self.minute:02d}:{self.second:02}'

    def __add__(self, other_time):
        new_time = Time()

        # Second track
        if (self.second + other_time.second) > 59:
            self.minute += 1
            new_time.second = self.second + other_time.second - 60
        else:
            new_time.second = self.second + other_time.second

        # Minute track
        if (self.minute + other_time.minute) > 59:
            self.hour += 1
            new_time.minute = self.minute + other_time.minute - 60
        else:
            new_time.minute = self.minute + other_time.minute

        # Hour track
        if (self.hour + other_time.hour) > 23:
            new_time.hour = self.hour + other_time.hour - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time


def main():
    time_1 = Time(32, 20, 30)
    print(time_1)
    time_2 = Time(1, 30, 20)
    print(time_1 + time_2)


main()
