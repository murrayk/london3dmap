import os
import fnmatch
import shutil


shutil.rmtree("/home/murray/temp/london", True)

def unzip_pbfs():

    for root, dir, files in os.walk("/home/murray/temp/london"):


        for item in fnmatch.filter(files, "*.pbf"):
            f = root + "/" + item


            t = os.system("gzip -d -S .pbf " + f)

def rename_pbfs():
    for root, dir, files in os.walk("/home/murray/temp/london"):

        for item in fnmatch.filter(files, "*"):
            f = root + "/" + item
            os.rename(f, f + '.pbf')

def extract_mbtiles():
    os.system("mb-util --image_format=pbf /home/murray/temp/london.mbtiles /home/murray/temp/london")


extract_mbtiles()
unzip_pbfs()
rename_pbfs()
