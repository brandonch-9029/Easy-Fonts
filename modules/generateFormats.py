import modules.convert

# converts the original file into other formats then copies it to the new directory

def convertTTF(fontfile):
    modules.convert.TTFtoWOFF(fontfile)
    modules.convert.TTFtoWOFF2(fontfile)

def convertWOFF(fontfile):
    newTTFname = modules.convert.WOFFtoTTF(fontfile)
    modules.convert.WOFFtoTTFtoWOFF2(newTTFname)

def convertWOFF2(fontfile):
    newTTFname = modules.convert.WOFFtoTTF(fontfile)
    modules.convert.WOFF2toTTFtoWOFF(newTTFname)