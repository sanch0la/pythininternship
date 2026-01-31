""""
a) Function to convert °C to °F
b) Function to classify temperature
c) Apply to a list of temperatures
"""

import sys


def main():
    temperature = int(input("Enter the temperature: "))

    def temperature_conversion(temperature):
        fahrenheit_temperature = temperature * 9 / 5 + 32
        return fahrenheit_temperature

    temperature_conversion(temperature)
    print(f"The temperature in Fahrenheit is {temperature_conversion(temperature)}")

    def classify_temperature(temperature):
        fahrenheit_temperature = temperature * 9 / 5 - 32
        if fahrenheit_temperature >= 70:
            return "Temperature too high"
        elif 70 > fahrenheit_temperature >= 50:
            return "Temperature is ok"
        else:
            return "Temperature is too low"

    print(f"The temperature in Fahrenheit is {temperature_conversion(temperature)}")

    classify_temperature(temperature)
    print(classify_temperature(temperature))

    return 0


if __name__ == '__main__':
    sys.exit(main())
