import convert
import shutil

# converts the original file into other formats then copies it to the new directory

def convertTTF(fontfile,foldername):
    convert.TTFtoWOFF(fontfile,foldername)
    convert.TTFtoWOFF2(fontfile,foldername)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)

def convertWOFF(fontfile,foldername):
    newTTFname = convert.WOFFtoTTF(fontfile,foldername)
    convert.WOFFtoTTFtoWOFF2(newTTFname)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)

def convertWOFF2(fontfile,foldername):
    newTTFname = convert.WOFFtoTTF(fontfile,foldername)
    convert.WOFF2toTTFtoWOFF(newTTFname)
    shutil.copyfile(fontfile, foldername + '/' + fontfile)