import os
import shutil

for root, dirs, files in os.walk(r'D:\OFFIS\Testing\wdex'):
    for f in files:
        if f.endswith(".jpg"): 
            old_path= os.path.join(root, f)
            dst = r'D:\OFFIS\Testing\Backup'
            new_path = os.path.join(dst, f)

            shutil.copy(old_path, new_path)

            res = r'D:\OFFIS\Testing\r_backup'
            shutil.move(root, res)

   
print("copy done")