import os, generateCSS, generateFormats

fontfile = "Ubuntu-Regular.woff2"
foldername = "uniquefolder"
fontname = "Ubuntu"

def main(fontfile, foldername, fontname):
    os.mkdir(foldername)
    fileext = str(os.path.splitext(fontfile)[1])

    if fileext == ".ttf":
        generateFormats.convertTTF(fontfile,foldername)

    elif fileext == ".woff":
        generateFormats.convertWOFF(fontfile,foldername)

    elif fileext == ".woff2":
        generateFormats.convertWOFF2(fontfile,foldername)
    
    generateCSS.generateCSS(fontfile, fontname, foldername)

main(fontfile,foldername,fontname)