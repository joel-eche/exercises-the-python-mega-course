"""
Here is a tricky exercise.

Please download the ZIP file in the Resources and unzip it in a folder.
Then create a script that merges the three text files into a new text
file containing the text of all three files. The filename of the merged
text file should contain the current timestamp down to the millisecond
level. E.g. "2016-06-01-13-57-39-170965.txt".
"""
import datetime

with open(str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f"))+'.txt', 'w+') as fileOut:
    #file1 in Sample-Files
    for i in range (1,4):
        file=open('Sample-Files/file' + str(i) + '.txt' , 'r')
        fileOut.write(file.read()+'\n')
        file.close()

a=input('Press any key to exit')
