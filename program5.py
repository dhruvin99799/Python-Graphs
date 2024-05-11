import pylab as py
py.figure(1)
x1=[10,20,30,40,50]
y1=[50,30,40,10,20]
x2=[10,20,30,40,50]
y2=[30,50,40,20,10]
py.xlabel('Data')
py.ylabel('Production')
py.plot(x1,y1,color='red',linewidth='2')
py.plot(x2,y2,color='green',linewidth='3')
py.legend()
py.show()
