# E is egg
# M is tm/tr
# T is tutor 
# L(number) is level
# S(number) is event
# V is virtual console

# -=-

# isolate letters
def isoletters(__str = ""):
    for _a in __str:
        if not _a.isalpha():
            __str = __str.replace(_a,"")
    return __str

# search in list
def searchlist(__search, __lst = []):
    __a = 0
    while __a < len(__lst):
        if __search in __lst[__a]:
            return __a
        __a += 1
    return -1

        

# sourcePath = r"C:\Users\david\Downloads\Modding\Minecraft\showdownToCobblemon\bulbasaur.ts"
# s = open(sourcePath, "r")
# for x in s:
#     print(x.replace("	",""))
# s.close()

a = ""
currentLine = ""
currentList = []
currentListGroup = []

currentLine = '			doubleedge: ["9M", "8L33", "8V", "7L27", "7V", "6L27", "5L27", "4L27", "3M"],'
print(currentLine)
currentList = currentLine.split('"')
# turn typescript list into python list
for a in currentList:
    if not a.isalnum():
        currentList.remove(a)
print(currentList)
# sort list for most valuable tag and add to list as needed;
# levelup > TM > egg > tutor > event (no event moves for now)
priorityBracket = ["level", "tm", "egg", "tutor", "event"]
a = ""
for a in currentList:
    print(a)
    print(isoletters(a))
    print(currentListGroup)
    print(searchlist("level",currentListGroup))
    print("")
    match isoletters(a):
        case "L":   # levelup moves at highest priority,
            if searchlist("level",currentListGroup) == -1:
                currentListGroup.append("level" + a[2:])
        case "M":   # followed by TMs,
            currentListGroup.append("tm")
        case "E":   # then egg moves,
            currentListGroup.append("egg")
        case "T":   # then tutor moves,
            currentListGroup.append("tutor")
        case "S":   # then finally event moves, which are currently grounded on psychic terrain and thus immune to the priority bracket
            print("Event move ping; not added to list. Fix later")
print(currentListGroup)
currentListGroup = list(set(currentListGroup))      # remove duplicates in list,
print(currentListGroup)
for a in priorityBracket:                           # then filter out everything that isnt the highest on the priority bracket on the list
    if searchlist(a,currentListGroup) != -1:
        currentListGroup = currentListGroup[searchlist(a,currentListGroup)]
        break
# if len(currentListGroup) > 1:
#     currentListGroup = currentListGroup[0]
print(currentListGroup)