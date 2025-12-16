# List of lambda functions for unit conversions
converters = [
    lambda tonnes: tonnes * 1000,          # tonnes to kilograms
    lambda kg: kg * 1000,                   # kilograms to grams
    lambda g: g * 1000,                     # grams to milligrams
    lambda mg: mg / 453592.37               # milligrams to pounds
]

# User input in tonnes
tonnes = float(input("Enter weight in tonnes: "))

# Apply conversions
kg = converters[0](tonnes)
g = converters[1](kg)
mg = converters[2](g)
lbs = converters[3](mg)

# Output results
print(f"{kg} kg")
print(f"{g} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")
