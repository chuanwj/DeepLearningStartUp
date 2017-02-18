
from sys import argv
script,input_file = argv


def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

cur_file = open(input_file)

print("First let's print the whole file:\n")

print_all(cur_file)

print("Now,let's rewind,kind of like a tape.")
rewind(cur_file)


print("let's print three lines:")

cur_line =1
print_a_line(cur_line,cur_file)

cur_line = cur_line + 1
print_a_line(cur_line,cur_file)

cur_line = cur_line + 1
print_a_line(cur_line,cur_file)