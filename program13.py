import pylab as py
py.figure(1)
x=py.bar(['JAVA','PYTHON','PHP','JAVASCRIPT','C#','C++'],[22.2, 17.6, 8.8, 8, 7.7, 6.7])
# y=py.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
# py.bar(x)
x[0].set_color('green')
x[1].set_color('orange')
x[2].set_color('red')
x[3].set_color('black')
x[4].set_color('gray')
x[5].set_color('pink')
py.show()   