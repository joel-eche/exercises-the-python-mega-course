"""
Consider the following list:

temperatures=[10,-20,-289,100]

Then, iterate over the temperature converter function that you created in execise 3 and print
out the following output.
50.0
-4.0
That temperature doesn't make sense!
212.0
"""

def celciusToFahrenheit(celcius):
    if celcius >= -273.15:
        return celcius*(9/5)+32
    else:
        return "That temperature doesn't make sense!"

temperatures=[10,-20,-289,100]

for temperature in temperatures:
    print(celciusToFahrenheit(temperature))

a=input()
