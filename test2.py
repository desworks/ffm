import os

currentpath = os.path.dirname(os.path.abspath(__file__))

if os.path.isdir(currentpath + '\\out') is False:
    os.mkdir(currentpath + '\\out')
else:
    print('dir vorhanden')