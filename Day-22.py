temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C , F ): ").strip().upper()

# conversion
if unit == 'C':
    converted = temperature * 9 / 5 + 32
    print(f"{temperature}°C = {converted:.2f}°F")
elif unit == 'F':
    converted = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {converted:.2f}°C")
else:
    print("Please enter 'C' or 'F'.")