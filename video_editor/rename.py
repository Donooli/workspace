import os
import shutil

for path, dirs, files in os.walk('E:\\seongwon\\img\\slice_images-2\\choice\\pigimg'):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.png':
            afilename = filename[9:]
            print(afilename)
            shutil.move(f'E:\\seongwon\\img\\slice_images-2\\choice\\pigimg\\{filename}',f'E:\\seongwon\\img\\slice_images-2\\choice\\pigimg\\{afilename}')