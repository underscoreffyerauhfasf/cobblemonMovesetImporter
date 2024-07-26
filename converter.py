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

# initialize variables
priorityBracket = ["level", "tm", "egg", "tutor", "event"]

a = ""
currentMove = ""
currentMoveData = ""
currentPokemon = ""
currentLine = ""
currentList = []
currentListGroup = []
lineOutput = ""
lastLine = ""
movesToChange = []

sourcePath = r"C:\Users\david\OneDrive\Documents\Programming\Python\cobblemonMovesetImporter\bulbasaur.ts"
sourceFile = open(sourcePath, "r")
itrMove = False
for x in sourceFile:
    # second round of inits
    currentList = []
    currentListGroup = []
    currentMoveData = ""

    if "learnset:" in x:
        currentPokemon = lastLine.split(":")[0]
        currentPokemon = "".join(filter(str.isalnum, currentPokemon))
        print(currentPokemon)
        lastLine = x

        itrMove = True
        print("itrMove = True")
        continue
    lastLine = x

    if "}," in x:
        if itrMove == True:
            print("itrMove = False")
        itrMove = False
        continue

    if itrMove == False:
        continue
    #print(x)

    currentLine = x#'			doubleedge: ["9M", "8L33", "8V", "7L27", "7V", "6L27", "5L27", "4L27", "3M"],'

    # get the name of the move being operated on
    currentMove = currentLine.split(':')[0]
    currentMove = "".join(filter(str.isalnum, currentMove))

    # turn typescript list into python list
    currentList = currentLine.split('"')
    for a in currentList:
        if not a.isalnum():
            currentList.remove(a)
    print(currentList)

    # sort list for most valuable tag and add to list as needed;
    # levelup > TM > egg > tutor > event* (no event moves for now)
    a = ""
    for a in currentList:
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
            case "S":   # then finally event moves, which will be considered as tutor moves until cobblemon has a precedent
                currentListGroup.append("tutor")
                print("Event move ping; added to list as a tutor move. Address later")
            case "V":   # Virtual console here for posterity; will address when Cobblemon has a precedent
                print("Virtual console ping; wtf is going on here")
    currentListGroup = list(set(currentListGroup))      # remove duplicates in list,
    for a in priorityBracket:                           # then filter out everything that isnt the highest on the priority bracket on the list
        if searchlist(a,currentListGroup) != -1:
            print("Priority bracket ping")
            print(a)
            currentMoveData = currentListGroup[searchlist(a,currentListGroup)]
            break

    print(currentListGroup)
    print(currentMoveData)
    if currentMoveData == "":
        continue

    # dump into cobblemon json format
    for a in priorityBracket:   # "level", "tm", "egg", "tutor", "event"
        if a in currentMoveData:
            match a:
                case "level":
                    lineOutput = currentMoveData[5:]+":"+currentMove
                case _:
                    lineOutput = a+":"+currentMove
            break
    # debug for proper sorting
    if lineOutput[1] == ":":
        lineOutput = "0"+lineOutput

    print(lineOutput)
    movesToChange.append(lineOutput)
    print(currentLine)
movesToChange.sort()
print(movesToChange)
sourceFile.close()
