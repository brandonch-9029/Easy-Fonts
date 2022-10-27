import os

def generateCSS(filename, familyname, foldername):

    cssFile = str(os.path.splitext(filename)[0]) + ".css"

    folderlength = len(foldername) + 1
    filenameextract = str(os.path.splitext(filename)[0])
    filenameextract = filenameextract[folderlength:]

    template = "@font-face {\
        \n\tfont-family: '" + familyname + "';\
        \n\tsrc: url('" + filenameextract + ".woff2') format('woff2'),\
        \n\turl('" + filenameextract + ".woff') format('woff'),\
        \n\turl('" + filenameextract + ".ttf') format('truetype');\
        \n\tfont-style: normal;\
        \n\tfont-weight: normal;\
        \n\tfont-display: swap;\
        \n}\n\n"

    open(cssFile, "a").writelines(template)
