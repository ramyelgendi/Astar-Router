import matplotlib.pyplot as plt
import AStar
import numpy as np

plt.figure()
plt.axes(projection='3d')

test = AStar.AStar(1,1000,1000)
a, b, c = test.Path(1, 10, 20, 2, 30, 50)
d, e, f = test.Path(2, 100, 200, 1, 300, 50)
g, h, i = test.Path(1, 100, 50, 2, 300, 150)

print(" Path : ", a)
print(" g : ", b)
print(" f : ", c)
print(" ")

print(" Path : ", d)
print(" g : ", e)
print(" f : ", f)

print("\n")
paths = [a,d,g]
for i in paths:
    print(i)
    plt.plot([v[0] for v in i], [v[1] for v in i], [v[2] for v in i])

plt.show()
