import pylab
pylab.figure(1)
class data():
    def data1(s):
        id = dict()
        for i in range(1):
            values=[]
            n1=int(input("Enter Value Of Id = "))
            for i in range(n1):
                value = int(input("Enter Value Of Chart = "))
                values.append(value)
                a = n1+1
            print("Value Is = ",values)
            
            
            

            
            

            pylab.bar(a,values)
            pylab.xlabel("Id")
            pylab.ylabel("Values")
            pylab.title("Data Information")

obj = data()
obj.data1()
pylab.show()

