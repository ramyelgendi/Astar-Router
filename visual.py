# Library
import matplotlib.pyplot as plt


class visual():
    def __init__(self, pathsList):  # Class Constructor
        self.pathsList = pathsList

    def figure(self):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        for i in self.pathsList:
            ax.plot([v[0] for v in i], [v[1] for v in i], [v[2] for v in i])
        ax.set_xlabel('Width')
        ax.set_ylabel('Height')
        ax.set_zlabel('Layers')
        ax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        ax.set_yticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
        ax.set_zticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        plt.title("A* Router Simulation\n")
        plt.show()
