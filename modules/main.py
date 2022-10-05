import os, generateCSS, generateFormats

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

main('Ubuntu-Regular.ttf','testfolder','Ubuntu')