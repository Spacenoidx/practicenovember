voltage= 120
current = 13

resistance = .004
length = input("Enter your cable length.")

wattage = (voltage * current)
limiter = resistance * int(length)
wattage = wattage / limiter

print(wattage)

