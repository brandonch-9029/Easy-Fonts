import modules.convert

# converts the original file into other formats then copies it to the new directory

def convertTTF(fontfile,foldername):
    modules.convert.TTFtoWOFF(fontfile,foldername)
    modules.convert.TTFtoWOFF2(fontfile,foldername)

def convertWOFF(fontfile,foldername):
    newTTFname = modules.convert.WOFFtoTTF(fontfile,foldername)
    modules.convert.WOFFtoTTFtoWOFF2(newTTFname)

def convertWOFF2(fontfile,foldername):
    newTTFname = modules.convert.WOFFtoTTF(fontfile,foldername)
    modules.convert.WOFF2toTTFtoWOFF(newTTFname)