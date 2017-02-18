from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("copy from %s to %s" % (from_file,to_file))

in_file = open(from_file)
in_data = in_file.read()


print("The input file is %d bytes long" % len(in_data))

print("Does the output file exists? %s" % exists(to_file))

print("Ready,hit Enter to cintiunue,CTRL-C to abort")
input()

out_file = open(to_file,'w')
out_file.write(in_data)

print("Alright,all done")

out_file.close()
in_file.close()