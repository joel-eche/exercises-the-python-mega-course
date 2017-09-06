with open('example.txt','a+') as file:
    file.seek(0)
    content=file.read()
    file.write('\nHello line')

print(content)
