
def add(a,b):
    print("Add %d + %d" % (a,b))
    return a+b

def subtract(a,b):
    print("Subtract %d - %d "%(a,b))
    return a - b

def multiply(a,b):
    print("multiply %d * %d" %(a,b))
    return a*b

def divide(a,b):
    print("Divide %d / %d"%(a,b))
    return a/b

print("Let's do some math with just functions")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age:%d, Height: %d, Weight: %d, IQ: %d"%(age,height,weight,iq))


what = add(age,subtract(height,multiply(weight,divide(iq,2))))
print("That becomes:", what)