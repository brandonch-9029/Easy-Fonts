from fontTools import ttLib

fontPath = "input.ttf"

font = ttLib.TTFont(fontPath)
fontFamilyName = font['name'].getDebugName(1)
fullName= font['name'].getDebugName(4)

print(fontFamilyName)
print(fullName)