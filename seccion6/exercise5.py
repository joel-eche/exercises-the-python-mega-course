"""
Here's a rather challenging exercise that integrates functions,
loops, conditionals, and file handling.
In exercise 4, you recursively printed out converted temperature in the command line.
For this exercise, please consider the same list of Celsius values again as input:

temperatures=[10,-20,-289,100]

Try to make a script that converts Celsius to Fahrenheit and creates a text file and
stores the converted values inside the text file. Your text file content should look
like this:

50.0
-4.0
212.0

Please don't write any message in the text file when input is lower than -273.15.
"""

def celciusToFahrenheit(celcius):
    if celcius >= -273.15:
        return celcius*(9/5)+32

temperatures=[10,-20,-289,100]

with open('temperatures.txt','w+') as file:
    for temperature in temperatures:
        file.write(str(celciusToFahrenheit(temperature)) + '\n')

    file.seek(0)
    file.read()

a=input()
