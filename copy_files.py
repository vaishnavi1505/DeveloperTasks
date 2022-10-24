## @vaishnavi1505 Date: 24/02/2022

## to copy all .jpg files from source folder to destination folder and then keeping the backup file in one r_backup folder
## automation of process with python

import os
import shutil


for root, dirs, files in os.walk(r'D:\work\Testing\wdex'):     
    for f in files:
        if f.endswith(".jpg"): 
            old_path= os.path.join(root, f)     #source folder
            dst = r'D:\work\Testing\Backup'     
            new_path = os.path.join(dst, f)     #Destination folder

            shutil.copy(old_path, new_path)     #copy function

            res = r'D:\work\Testing\r_backup'   #backup path
            shutil.move(root, res)              #move function

   
print("copy done")
