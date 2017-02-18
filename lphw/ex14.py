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

from sys import argv
scr, user_name = argv
prompt = ">>"

print ("hi %s, I'm the %s script." % (user_name,scr))

print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)

## no more support raw_input
likes = input(prompt)
print ("Where do you live %s?" % user_name)
lives = input(prompt)
print ("What kind of computer do you have?")
computer = input(prompt)
print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer) )

num = input('enter your age')
print (type(num))

