import pylab
pylab.figure(1)
x=pylab.array(['October 3, 2016','October 4, 2016','October 5, 2016','October 6, 2016','October 7, 2016'])
y=pylab.array([50,60,80,70,55])
pylab.xlabel('Date')
pylab.ylabel('Financial Data')
pylab.plot(x,y,color="red")
pylab.show()