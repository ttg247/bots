#import module 
import os
import pathlib

#folder directory path
path = "C:\\Users\\LAPTOP\\Documents\\sj\\img\\"

#rename each file in directory
def rname(a):
    for count, filename in enumerate(os.listdir(a)):
        dst =  "img" + str(count) 
        src = a + filename
        dst = a + dst + ".png"

        os.rename(src, dst)

#list all files in image folder
for (root, dirs, files) in os.walk(path, topdown = True):
    for name in dirs:
        paths = os.path.join(root, name)
        pathz = paths + "\\"
        print(pathz) 
        if os.path.isdir(pathz):
            rname(pathz) 

