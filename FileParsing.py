# Ramy ElGendi
# 900170269

# Libraries
import os.path


class FileParsing:
    def __init__(self, filename):  # Class Constructor
        self.filename = filename
        self.netList = []
        self.netNames = []

    def Exists(self):
        if os.path.isfile(self.filename):
            print(self.filename + " has been imported!")
            return True
        return False

    def Parse(self):
        file = open(self.filename, 'r')
        lines = file.readlines()

        for line in lines:  # net1 (1, 10, 20) (2, 30, 50) (1, 5, 100)
            netList = []
            self.netNames.append(line[:line.index('(')])
            modified = line[line.index('(') + 1:].split('(')
            for x in modified:
                if ')' in x:
                    i = x.replace(')', '')
                if '\n' in i:
                    i = i.replace('\n', '')
                netList.append(i.split(','))
            self.netList.append(netList)

        return self.netList

    def OutputList(self, pathsList,file_out):
        out = open(file_out, "w")
        for i,line in enumerate(pathsList):
            out.write(self.netNames[i]+" ")
            for path in line:
                out.write("("+str(path[2]) + " "+str(path[0]) + " "+str(path[1]) + ") ")

            out.write("\n")


        return True
