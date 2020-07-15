import FileParsing
import sys
import AStar
import visual
inputFile = input("Enter address for your input file. [Format: /Users/ramyelgendi/Desktop/AStarRouter/input.txt] :\n")
# Parsing Input
file = FileParsing.FileParsing(inputFile)
if not file.Exists():
    print("Parsing file does not exist!")
    sys.exit()
netList = file.Parse()
print("Input has been parsed successfully!")

# Create Grid
router = AStar.AStar(1, 1000, 1000,6)

pathsList = []
print("Beginning simulation!")
for line in netList:
    Path = []
    for i, node in enumerate(line):
        try:
            source = node
            target = line[i + 1]
            netPath = router.Path(int(source[0]), int(source[1]), int(source[2]), int(target[0]), int(target[1]),
                                        int(target[2]))
            Path = Path + netPath
        except IndexError:
            pass
    pathsList.append(Path)

# Writing Output
outputFile = inputFile.replace('.txt', '_out.txt')
status = file.OutputList(pathsList, outputFile)
if status:
    print("Completed Successfully! ")

    while True:
        choice = input("Do you want to see results on a graph? (yes/no): \n")
        if choice == "yes":
            visual = visual.visual(pathsList)
            visual.figure() # Draw
            sys.exit()
        elif choice == "no":
            sys.exit()
        else:
            print("Invalid Entry! Please type yes/no only")


else:
    print("Failed! ")
    sys.exit()
