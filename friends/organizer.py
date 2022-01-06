"""

Task: Organize files of a folder
Description:
          In this task, you will write a python function named `organize` which will have two arguments `source_folder` & `dest_folder`. The function will iterate over all the files of the source directory and, copy these files in the `dest_folder` separating each type of file in different folder.

"""
import glob
import os
import shutil

def organize(source_dir, dest_dir):
    source = source_dir
    dirs = os.listdir(source)
    for file in dirs:
        if file.endswith(".html"):
            if not os.path.exists(dest_dir+"/html/"):
                os.makedirs(dest_dir+"/html/")
            shutil.copy(source_dir+"/"+file,dest_dir+"/html/")

        elif file.endswith(".css"):
            if not os.path.exists(dest_dir+"/css/"):
                os.makedirs(dest_dir+"/css/")
            shutil.copy(source_dir+"/"+file,dest_dir+"/css/")

        elif file.endswith(".js"):
            if not os.path.exists(dest_dir+"/js/"):
                os.makedirs(dest_dir+"/js/")
            shutil.copy(source_dir+"/"+file,dest_dir+"/js/")

        elif file.endswith(".py"):
            if not os.path.exists(dest_dir+"/py/"):
                os.makedirs(dest_dir+"/py/")
            shutil.copy(source_dir+"/"+file,dest_dir+"/py/")

if __name__ == "__main__":
    organize("source_dir","dest_dir")
