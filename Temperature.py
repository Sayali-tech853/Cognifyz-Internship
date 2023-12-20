#Create a Python program that converts temperatures between Celsius and Fahrenheit. Prompt the user to enter a
#temperature value and the unit of measurement, and then display the converted temperature.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {converted_temperature:.2f} Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {converted_temperature:.2f} Celsius")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()