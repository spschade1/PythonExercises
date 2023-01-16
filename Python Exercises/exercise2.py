#Temperature Conversion

def convertToFahrenheit(degreesCelsius):
    x = degreesCelsius * (9/5) + 32
    return x


def convertToCelsius(degreesFahrenheit):
    x = (degreesFahrenheit - 32) * (5/9)
    return x


print(convertToFahrenheit(0))
print(convertToCelsius(0))
print(convertToCelsius(convertToFahrenheit(42)))


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223 
assert convertToFahrenheit(0) == 32 
assert convertToFahrenheit(100) == 212 
assert convertToCelsius(convertToFahrenheit(15)) == 15 
# Rounding errors cause a slight discrepancy: 
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

