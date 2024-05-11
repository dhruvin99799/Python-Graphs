import pylab as py
py.figure(1)
x=py.array(['JAVA','PYTHON','PHP','JAVASCRIPT','C#','C++'])
y=py.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
py.bar(x,y,color='green')
py.show()