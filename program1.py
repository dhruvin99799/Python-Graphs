import pylab
pylab.figure(1)
x=pylab.array(['Apple','Banana','Orange','Watermelan','Payneple'])
y=pylab.array([10,20,30,40,50])
pylab.xlabel('Fruits')
pylab.ylabel('Production')
pylab.plot(x,y,color="pink")
pylab.show()