import sys
import medals
import total
data_file = sys.argv[1]
with open("data_file.tsv", 'r') as file:
    lines = file.readlines()
    next_line = file.readlines()


mode = sys.argv[2]  # medals or total

if mode == "-total":
    total.total()
elif mode == "-medals":
    medals.medals()
