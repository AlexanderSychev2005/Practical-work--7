import sys
import medals
import total

#def total():
 #   year = sys.argv[3]
 #    for line in lines:
 #        line = line.split("\t")
 #        if year == line[9]:
 #            print(line)

data_file = sys.argv[1]
with open("data_file.tsv", 'r') as file:
    lines = file.readlines()
    next_line = file.readlines()


mode = sys.argv[2]  # medals or total

if mode == "-total":
    total.total()
elif mode == "-medals":
    medals.medals()
