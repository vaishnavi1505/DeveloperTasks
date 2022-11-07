import os

folder = r'D:\OFFIS\Green\Results'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name

     source = folder +'\\'+ file_name

    # Adding the count to the new file name and extension
     destination = folder + '\\' + str(count) + '.xlsx'
     print(destination)

    # Renaming the file
     os.rename(source, destination)
     count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)