def celcius_to_fahrenheit(T):
    """Convert temperature from Celcius to Fahrenheit"""  # This line is a 'docstring' explaining the function. 
    return T*9/5 + 32

# Temperature conversion formulas:
# https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature

# Task: Create functions to convert from Celcius to the following scales. 
# Give your function a docstring. 

# Kelvin

# Rankine

# Delisle 

# Newton

# Réaumur

# Rømer


def main():
    temperature_degreeC = 21.7
    print(f"The temperature in Celcius is: {temperature_degreeC} C")

    temperature_degreeF = celcius_to_fahrenheit(temperature_degreeC)
    print(f"The temperature in Fahrenheit is: {temperature_degreeF} F")

    # Task: Print the output of your function. 

# When you run this script from the command line, e.g. 'python convert_temperature.py' 
# it will execute the block below:
if __name__ == "__main__":
    main()
