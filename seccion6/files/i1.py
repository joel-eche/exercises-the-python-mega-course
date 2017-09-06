file=open('example.txt')
print(type(file))
print()
content=file.read()
print(content)
print(type(content))

content=file.readlines()
print(content)

print()
file.seek(0)
content=file.readlines()
print(content)

print()
content=[i.rstrip('\n') for i in content]
print(content)

file.close()
