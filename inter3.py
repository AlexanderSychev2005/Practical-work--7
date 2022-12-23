import sys
import overall
def interactive():
    file = sys.argv[1]
    country_name = input("Please, enter a country: ")
    first_year_olimp = None
    first_place_olimp = None
    years = []
    gold_count = 0
    silver_count = 0
    bronze_count = 0
    with open(file, "r") as file:
        line = file.readline()
        while line:
            line_after_split = line.split("\t")
            country_line1 = line_after_split[7]
            # country_line2 = line_after_split[8]
            medal_line = line_after_split[-1][:-1]
            year_line = line_after_split[9]
            city_line = line_after_split[-4]
            team_line = line_after_split[6]
            if (country_line1 == country_name or team_line == country_name) and year_line not in years:
                years.append(year_line)
            if (country_line1 == country_name or team_line == country_name) and medal_line != "NA":
                if medal_line == "Gold" and year_line in years:
                    gold_count += 1
                elif medal_line == "Silver" and year_line in years:
                    silver_count += 1
                elif medal_line == "Bronze" and year_line in years:
                    bronze_count += 1
                if (country_line1 == country_name or team_line == country_name) and first_year_olimp is None:
                    first_year_olimp = year_line
                    first_place_olimp = city_line
                elif (first_year_olimp is not None and country_line1 == country_name or team_line == country_name) and year_line < first_year_olimp:
                    first_year_olimp = year_line
                    first_place_olimp = city_line
            line = file.readline()
    average_gold_medals = gold_count / len(years)
    average_silver_medals = silver_count / len(years)
    average_bronze_medals = bronze_count / len(years)
    print(f"First olympiade for {country_name} was in {first_year_olimp} and that was in {first_place_olimp}")
    dict_values, dict_keys = overall.overall([country_name])
    min_medals = min(dict_values)
    print(f"The fewest medals {country_name} earned in {dict_keys[dict_values.index(min_medals)]}'s year and the number was {min_medals}")
    print(f"Average number of gold medals: {average_gold_medals}\nAverage number of silver medals: {average_silver_medals}\nAverage number of bronze medals: {average_bronze_medals}")