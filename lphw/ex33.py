#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      jcwang
#
# Created:     02/01/2017
# Copyright:   (c) jcwang 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

i = 0
numbers = []

while i < 10:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("number now :"), numbers
    print ('At the buttom is %d' % i)

print ("The numbers :")
for num in numbers:
    print ("num")

for i in range(0,10):
    print ("list i is %d" % i)