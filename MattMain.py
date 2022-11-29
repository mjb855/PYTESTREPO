import MattFunct as mf
import matplotlib.pyplot as pyplot

print("The Result: ", mf.MattMult(2, 3))
print("The Result: ", mf.MattDiv(10, 0))
print("The Result: ", mf.MattDiv(10, 5))
print("The Result: ", mf.MattAdd(101, 9))

pyplot.plot((0,1,2,3),(0,1,3,0))
pyplot.show()
