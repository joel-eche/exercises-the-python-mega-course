"""
In exercise 1 you created a function that converted Celsius degrees to Fahrenheit.
The lowest possible temperature that physical matter can reach is -273.15 °C.
With that in mind, please improve the function by making it print out a message
in case a number lower than -273.15°C is passed as input when calling the function.
"""

def celciusToFahrenheit(celcius):
    return celcius*(9/5)+32

celcius=float(input("Enter Celcius: "))

if celcius >= -273.15:
    print("Fahrenheit: ",celciusToFahrenheit(celcius))
else:
    print("Is this possible?")

a=input()
