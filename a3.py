print("Temperature Converter")
print("Choose the input temperature unit:")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = input("Enter your choice (1/2/3): ")
temperature = float(input("Enter the temperature value: "))

if choice == "1":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print("Fahrenheit:", fahrenheit)
    print("Kelvin:", kelvin)

elif choice == "2":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print("Celsius:", celsius)
    print("Kelvin:", kelvin)

elif choice == "3":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)

else:
    print("Invalid choice. Please select 1, 2, or 3.")
