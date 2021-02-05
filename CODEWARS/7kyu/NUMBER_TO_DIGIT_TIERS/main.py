# 2017 ->  ["2", "20", "201", "2017"]

def create_array_of_tiers(n):
    n = str(n)
    m = []
    for index in range(len(n)):
        try:
            m += [str(n)[0:index + 1]]
        except IndexError:
            pass
    
    return m

print(create_array_of_tiers(2017))

