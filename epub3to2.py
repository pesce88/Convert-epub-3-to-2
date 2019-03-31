import glob, os
import zipfile

folder = "."
for filename in glob.iglob(os.path.join(folder, '*.epub')):
     #rename all file from epub to zip
     os.rename(filename, filename[:-4] + '.zip')
     
for filename in glob.iglob(os.path.join(folder, '*.zip')):
        print filename
        zip_ref = zipfile.ZipFile(filename, 'r')
        os.makedirs(filename[:-4])
        zip_ref.extractall(filename[:-4])
        zip_ref.close()

