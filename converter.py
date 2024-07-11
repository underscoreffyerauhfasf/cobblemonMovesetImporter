# E is egg
# M is tm/tr
# T is tutor 
# L(number) is level
# S(number) is event
# V is virtual console

# -=-

# sourcePath = r"C:\Users\david\Downloads\Modding\Minecraft\showdownToCobblemon\bulbasaur.ts"
# s = open(sourcePath, "r")
# for x in s:
#     print(x.replace("	",""))
# s.close()
currentLine = '			doubleedge: ["9M", "8L33", "8V", "7L27", "7V", "6L27", "5L27", "4L27", "3T"],'
print(currentLine)
currentList = currentLine.split('"')
#print(currentList)
for a in currentList:
    if not a.isalnum():
        currentList.remove(a)
print(currentList)