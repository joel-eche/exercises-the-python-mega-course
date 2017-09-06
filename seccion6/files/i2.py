file=open('example2.txt','w')

file.write('Line 1')
file.close()

file=open('example2.txt','w')
file.write('Line 1\n')
file.write('Line 2')
file.close()

file=open('example2.txt','a')
file.write('\nOther Line')
file.close()
