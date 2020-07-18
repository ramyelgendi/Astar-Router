# Ramy ElGendi
# 900170269

# Libraries
import sys

import numpy as np


class AStar:
    def __init__(self, via=1, height=1000, width=1000, layers=10):  # Class Constructor
        self.height = height
        self.width = width
        self.layers = layers
        self.via = via
        self.grid = np.empty([width, height], dtype=list)  # Creating a numpy array that accepts lists WHY NUMPY? Faster

        for x in range(height):  # Initializing Empty Grid
            for y in range(width):
                for z in range(layers + 1):  # Creating the amount of layers
                    if z == 0:
                        self.grid[x][y] = []
                    else:
                        self.grid[x][y] += [0]

    def H_Fn(self, x1, y1, z1, x2, y2, z2):  # xyz1s are the source, xyz2s are the target
        return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

    def Next(self, x1, y1, z1, x2, y2, z2):  # xyz1s are the source, xyz2s are the target
        F_final = self.height * self.width
        Final = []
        if z1 == 1:  # Source Node is in layer 1
            if x1 - 1 >= 0 and self.grid[x1 - 1][y1][z1] != 1 and self.grid[x1 - 1][y1][z1 + 1] != 1:
                Final.append([x1 - 1, y1, z1 + 1])
            if x1 >= 0 and self.grid[x1][y1 - 1][z1 - 1] != 1:
                Final.append([x1, y1 - 1, z1])
            if x1 + 1 < self.height and self.grid[x1 + 1][y1][z1] != 1 and self.grid[x1 + 1][y1][z1 + 1] != 1:
                Final.append([x1 + 1, y1, z1 + 1])
            if y1 + 1 < self.width and self.grid[x1][y1 + 1][z1 - 1] != 1:
                Final.append([x1, y1 + 1, z1])
        elif z1 == 2:  # Source Node is in layer 2
            if z2 == 2:
                z = z2 - 1
            else:
                z = z2

            if x1 - 1 >= 0 and self.grid[x1 - 1][y1][z1 - 1] != 1:
                Final.append([x1 - 1, y1, z1])
            if y1 - 1 >= 0 and (self.grid[x1][y1 - 1][0] != 1 or self.grid[x1][y1 - 1][2] != 1):
                Final.append([x1, y1 - 1, 1])
            if x1 + 1 < self.height and self.grid[x1 + 1][y1][1] != 1:
                Final.append([x1 + 1, y1, z1])
            if y1 + 1 < self.width and (self.grid[x1][y1][0] != 1 or self.grid[x1][y1 + 1][2] != 1):
                Final.append([x1, y1 + 1, z])

        else:  # Support for multi layer (NOT TESTED)
            if x1 - 1 >= 0 and self.grid[x1 - 0][y1][z1 - 3] != 1 and self.grid[x1 - 1][y1][z1 - 2] != 1:
                Final.append([x1 - 1, y1, z1 - 1])
            if y1 - 1 >= 0 and self.grid[x1][y1 - 1][z1 - 1] != 1:
                Final.append([x1, y1 - 1, z1])
            if x1 + 1 < self.height and self.grid[x1 + 1][y1][z1 - 3] != 1 and self.grid[x1 + 1][y1][z1 - 2] != 1:
                Final.append([x1 + 1, y1, z1 - 1])
            if y1 + 1 < self.width and self.grid[x1][y1 + 1][z1 - 1] != 1:
                Final.append([x1, y1 + 1, z1])

        if len(Final) == 0:
            return (x1, y1, z1), 0, 0
        else:
            for node in Final:
                if z1 == node[2]:
                    F = 1 + self.H_Fn(node[0], node[1], node[2], x2, y2, z2)
                else:
                    F = self.via + self.H_Fn(node[0], node[1], node[2], x2, y2, z2)

                if F < F_final:  # Picking the lowest
                    F_final = F
                    Node = node
                    G = F - self.H_Fn(node[0], node[1], node[2], x2, y2, z2)

        return Node, F_final, G

    def Path(self, z1, x1, y1, z2, x2, y2):
        # Initialization
        FinalPath = [[x1, y1, z1]]
        GCost = [0]
        H = [self.H_Fn(x1, y1, z1, x1, y1, z1)]
        F = [GCost[0] + H[0]]

        self.grid[x1][y1][z1 - 1] = 1

        CurrentNode = FinalPath[0]
        timeout = 0
        while not CurrentNode == [x2, y2, z2] and timeout < 1000000:
            timeout += 1
            # Check if target==source
            CurrentNode_, f, g = self.Next(CurrentNode[0], CurrentNode[1], CurrentNode[2], x2, y2, z2)

            CurrentNode = CurrentNode_
            self.grid[CurrentNode[0]][CurrentNode[1]][CurrentNode[2] - 1] = 1
            FinalPath.append(CurrentNode)
            F.append(f)
            GCost.append(g)
        if timeout < 1000000:
            return FinalPath
        else:
            return []
