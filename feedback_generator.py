# FEEDBACK_GENERATOR v.2.2
# Author: Patrick Fock
# 
# This generator creates feedback file for tutor courses using the console.
# Syntax: python feeback_generator.py <path of member file> <destination path> <points of exercise 1> ... <points of exercise n> <points of bonus exercise>
# If <path of member file> is "" or "default", a single feedback file "Bewertung_.txt" will be generated.
# If the last argument <points of bonus exercise> is a "0", the bonus exercise won't be created.
# __________________________________________________________________________________________________________________________________________________________
# 
# Example call: python feeback_generator.py "members.txt" "C:\Documents" 2 3 8
# This creates the following file content:
#
# AUFGABE 1
# ****************************************************************************************************
# Punkte: 0/2
#
# AUFGABE 2
# ****************************************************************************************************
# Punkte: 0/3
#
# BONUS
# ****************************************************************************************************
# Punkte: 0/8
#
# ****************************************************************************************************
# GESAMT 0/5 + BONUS 0/8


# importing sys to get console arguments in argv
from sys import argv as arguments


# sub method for creating a line of * as underline
def starline(amount_of_stars):
    res = ""
    for i in range(amount_of_stars):
        res += "*"
    return res + "\n"


# sub method for reading the member names from line by line from a file
def read_names(file):
    if file == "default" or file == "":
        return [""]
    else:
        name_file = open(file, "r")
        names = name_file.read().splitlines()
        name_file.close()
        for name in names:
            name.replace(" ", "_")
        return names


def main():
    names = read_names(arguments[1])
    # iteration over all members in the course
    for people in names:
        # save file content in variable content
        content = ""
        sum_points = 0
        # holds an additional bonus point string, if there are no bonus points, the string will be empty
        bonus_points = " + BONUS 0/" + str(arguments[len(arguments) - 1]) if int(arguments[len(arguments) - 1]) > 0  else ""
        stars = starline(85)
        # sets the destination path for the feedback files.
        path = "." if arguments[2] == "" else arguments[2]
        # iteration to create "Aufgabe" with the given amount of points
        for i in range(3, len(arguments)):
            # the last "Aufgabe" is named "Bonus" if bonus points > 0, otherwise the bonus exercise will not be created.
            if i == len(arguments) - 1 and int(arguments[i]) == 0:
                continue
            elif i == len(arguments) - 1 and int(arguments[i]) > 0:
                bonus = "BONUS "
            else:
                bonus = "AUFGABE " + str(i - 2)
                sum_points += int(arguments[i])
            content += bonus + "\n" + stars + "Punkte: 0/" + arguments[i] + "\n\n"
        content += stars + "GESAMT 0/" + str(sum_points) + bonus_points
        # generate one file for each member or default file and write content into it
        file = open(path + "\\Bewertung_" + people + ".txt", "w")
        file.write(content)
        file.close()


if __name__ == "__main__":
    main()
