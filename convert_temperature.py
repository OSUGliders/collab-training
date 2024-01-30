def celcius_to_fahrenheit(T):
    """Convert temperature from Celcius to Fahrenheit"""  # This line is a 'docstring' explaining the function. 
    return T*9/5 + 32

# Temperature conversion formulas:
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature

# Task: Create functions to convert from Celcius to the following scales. 
# Give your function a docstring. 

# Kelvin

def celcius_to_kelvin(T):
    return T + 273.15

# Rankine
def celsius_to_rankine(celsius):
    rankine = (celsius + 273.15) * (9/5)
    return rankine


# Delisle
def celsius_to_Delisle(celsius):
    Delisle = (100 - celsius) * (3/2)
    return Delisle

# Newton

def celcius_to_reaumur(T:float) -> float:
    ''' Convert C to Reaumur '''
    return T * 4/5

# Rømer


def main():
    temperature_degreeC = 21.7
    print(f"The temperature in Celcius is: {temperature_degreeC} C")

    temperature_degreeF = celcius_to_fahrenheit(temperature_degreeC)
    print(f"The temperature in Fahrenheit is: {temperature_degreeF} F")

    temperature_degreeK = celcius_to_kelvin(temperature_degreeC)
    print(f"The temperature in Kelvin is: {temperature_degreeK} K")
    temperature_degreeRe = celcius_to_reaumur(temperature_degreeC)
    print(f"The temperature in reaumur is: {temperature_degreeRe} Re")

    # Task: Print the output of your function. 

    print("Jesse added this.")

# When you run this script from the command line, e.g. 'python convert_temperature.py' 
# it will execute the block below:
if __name__ == "__main__":
    main()
