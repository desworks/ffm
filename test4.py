import os

currentpath = os.path.dirname(os.path.abspath(__file__)) + '\\'
print(currentpath)

for filename in os.listdir(".\\tst"):
    if filename.endswith('.flv.flv'):
        os.renames(currentpath + filename, currentpath + filename[:-8] + '.mp4')
    if filename.endswith('.flv'):
        os.renames(currentpath + filename, currentpath + filename[:-4] + '.mp4')
    if filename.endswith('.mpg'):
        os.renames(currentpath + filename, currentpath + filename[:-4] + '.mp4')
    if filename.endswith('.mpeg'):
        os.renames(currentpath + filename, currentpath + filename[:-5] + '.mp4')
    if filename.endswith('.avi'):
        os.renames(currentpath + filename, currentpath + filename[:-4] + '.mp4')
    if filename.endswith('.wmv'):
        os.renames(currentpath + filename, currentpath + filename[:-4] + '.mp4')