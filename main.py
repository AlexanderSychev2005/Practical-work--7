import sys
import interactive
import medals
import total
import overall

data_file = sys.argv[1]
with open("data-file.tsv", 'r') as file:
    lines = file.readlines()
    next_line = file.readlines()


mode = sys.argv[2]  # medals or total

if mode == "-total":
    total.total()
elif mode == "-medals":
    medals.medals()
elif mode == "-overall":
    overall.overall()
elif mode == "-interactive":
    interactive.interactive()


