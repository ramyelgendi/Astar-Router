# Ramy ElGendi

# Ramy ElGendi
# 900170269

# Libraries
import os.path

class InputParsing:
    def __init__(self, filename):  # Class Constructor
        self.filename = filename
        if not os.path.isfile(filename):
            print("ERROR! File doesn't exist!")
            return False

        return True


parse = InputParsing()