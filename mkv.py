import os
filename = input("What is the file name?")
path = 'A:\Downloads\\' + filename
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index+1), '.mkv'])))

