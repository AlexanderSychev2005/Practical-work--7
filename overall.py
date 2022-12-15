import sys

def overall():
    filename = sys.argv[1]
    countries = sys.argv[3:]
    dictionary = {}
    for country in countries:
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                line_after_split = line.split("\t")
                country_line = line_after_split[7]
                medal_line = line_after_split[-1][:-1]
                year_line = line_after_split[9]
                if year_line not in dictionary and country_line == country:
                    dictionary[year_line] = 0
                elif medal_line != "NA" and year_line in dictionary and country_line == country:
                    dictionary[year_line] += 1
                line = file.readline()
        dict_keys = [int(key) for key in dictionary.keys()]
        dict_values = [int(key) for key in dictionary.values()]
        maximum = max(dict_values)
        print(f'{country} - {maximum} - {dict_keys[dict_values.index(maximum)]}')
        dictionary.clear()
