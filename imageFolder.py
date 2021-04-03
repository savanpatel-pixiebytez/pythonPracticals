import fnmatch
import os
import shutil
import datetime

# Make new directory
try:
    os.mkdir(os.path.join('/Users/savanpatel/pixieBytez/python', 'img1'))
except OSError as error:
    pass

listOfFiles = os.listdir('/Users/savanpatel/pixieBytez/python/img1')
pattern = "*.svg"
imgArr = []
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        imgArr.append(entry)


# Renaming files
for i in range(0, len(imgArr)):
    Current_Date = datetime.datetime.today().strftime('%d-%b-%Y')
    os.rename(r'/Users/savanpatel/pixieBytez/python/img1/' + str(imgArr[i]),
              r'/Users/savanpatel/pixieBytez/python/img1/editName_' + str(i) + '.svg')


# Make new dir to copy images
try:
    os.mkdir(os.path.join('/Users/savanpatel/pixieBytez/python', 'editedImage'))
except OSError as error:
    pass
file_names = os.listdir('/Users/savanpatel/pixieBytez/python/img1')

pattern = "*.svg"

for file_name in file_names:
    if fnmatch.fnmatch(entry, pattern):
        shutil.copy(os.path.join('/Users/savanpatel/pixieBytez/python/img1',
                                 file_name), '/Users/savanpatel/pixieBytez/python/editedImage')
