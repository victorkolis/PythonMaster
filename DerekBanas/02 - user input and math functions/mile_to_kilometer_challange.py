# Miles => Kilometers

print('Welcome to the Mile to Kilometer converter.')
miles = int(input('Please enter the mileage: '))
CONVERSION_FACTOR = 1.60934
kilometers = miles * CONVERSION_FACTOR
print("{} miles equals {} kilometers".format(miles, kilometers))
