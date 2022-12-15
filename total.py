import sys
def total():
    dictionary ={
    }
    file = sys.argv[1]
    year = sys.argv[3]
    with open(file, "r") as file:
        # line = file.readline()
        line = file.readline()
        while line:
            line_after_split = line.split("\t")
            medal_line = line_after_split[-1][:-1]
            year_line = line_after_split[9]
            # country_line1 = line_after_split[6]
            country_line2 = line_after_split[7]
            if country_line2 and country_line2 in line_after_split:
                if medal_line != "NA":
                    if country_line2 not in dictionary and year_line == year:
                        dictionary[country_line2] = [0,0,0]
                    elif medal_line == "Gold" and year_line == year:
                        dictionary[country_line2][0] += 1
                    elif medal_line == "Silver" and year_line == year:
                        dictionary[country_line2][1] += 1
                    elif medal_line == "Bronze" and year_line == year:
                        dictionary[country_line2][2] += 1
            line = file.readline()
        for country, medals in dictionary.items():
            if medals != [0,0,0]:
                print(f"{country} - medals: gold {medals[0]}, silver {medals[1]}, bronze {medals[2]}  ")


