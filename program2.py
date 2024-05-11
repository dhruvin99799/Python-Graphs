import pylab
pylab.figure(1)
x=pylab.array(['Apple','Banana','Orange','Watermelan','Payneple'])
y=pylab.array([50,60,80,90,5])
pylab.xlabel('Fruits')
pylab.ylabel('Production')
pylab.plot(x,y,color="pink")
pylab.show()