# break_continue

# break stops the flow

spam = 0

while spam < 10:
    print(spam)
    spam += 1
    if spam == 7:
        break

##

print("\n\n")

##

# continue skips/bypass the flow

spam = 0

while spam < 10:
    spam += 1
    if spam == 2:
        continue
    else:
        print(spam)
        