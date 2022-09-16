from distutils import extension
import os
import shutil

from_dir="C:/Users/shwet/Downloads"
to_dir="C:/Users/shwet/OneDrive/Desktop/Downloadedimg"

listoffiles=os.listdir(from_dir)
#print(listoffiles)

for filename in listoffiles:
    name,extention=os.path.splitext(filename)
    # print(name)
    # print(extention)
    
    if extention=="":
        continue
    if extention in [".gif",".png",".jpg","jpeg","jfif"]:
        path1=from_dir+"/"+filename
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+filename
        # print("path1",path1)
        # print("path3",path3)
        if os.path.exists(path2):
            print("moving "+ filename+"..." )
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving "+ filename+"..." )
            shutil.move(path1,path3)

            