"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    courses = []
    for line in input_file:
        line = line.strip()
        course = line.split(',')
        course[2] = int(course[2])
        courses.append(course)
    input_file.close()
    return courses


def display_data(data):
    for subject_data in data:
        print("{} is taught by {} and has {} students".format(*subject_data))



main()


