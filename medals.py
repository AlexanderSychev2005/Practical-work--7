import sys


def medals():
    file = sys.argv[1]
    country = sys.argv[3]
    year = sys.argv[4]
    output_file = False
    optional_parameter = ""
    if len(sys.argv) >= 6:
        optional_parameter = sys.argv[5]
    if optional_parameter == "-output":
        if len(sys.argv) >= 7:
            target_file = sys.argv[6]
            open(target_file, "w").close()
            output_file = open(target_file, "a")
        else:
            print("In case of '-output' parameter target file name is required.")
            quit()

    counter = 0
    names = []
    medals = []
    is_country_exist = False
    is_year_exist = False
    with open(file, "r") as file:
        line = file.readline()
        while line:
            line_after_split = line.split("\t")
            medal_line = line_after_split[-1][:-1]
            sport_athlete = line_after_split[-3]
            name_athlete = line_after_split[1]
            if country in line_after_split:
                is_country_exist = True
                if year in line_after_split:
                    is_year_exist = True
                    while counter < 10:
                        if name_athlete not in names and medal_line != "NA":
                            counter += 1
                            print(f"{counter}, {name_athlete} - {sport_athlete} - {medal_line}")
                            if output_file:
                                output_file.write(f"{counter}, {name_athlete} - {sport_athlete} - {medal_line}\n")
                            names.append(name_athlete)
                        else:
                            break
                    medals.append(medal_line)
            line = file.readline()

    if not is_country_exist:
        print("Try another country")
        if output_file:
            output_file.write("Try another country")
        quit()
    if not is_year_exist:
        print("Try another year")
        if output_file:
            output_file.write("Try another year")
        quit()
    if counter < 10:
        print("It has less than 10 medalists")
        if output_file:
            output_file.write("It has less than 10 medalists")

    print("\nMedal summary:\nGold - ", medals.count("Gold"), " Silver - ", medals.count("Silver"), " Bronze - ",
          medals.count("Bronze"))
    if output_file:
        output_file.write(
            "\n\nMedal summary:\nGold - " + str(medals.count("Gold")) + " Silver - " + str(medals.count("Silver")) +
            " Bronze - " + str(medals.count("Bronze")))
    if output_file:
        output_file.close()

    file.close()




