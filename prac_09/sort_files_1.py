import os


def main():
    # change to FilesToSort directory
    os.chdir("FilesToSort")

    # print current directory path
    print(os.getcwd())

    # print a list of the files in the FileToSort directory to test working directory
    print(os.listdir('.'))

    # loop through each file in the directory
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        NewFiles1 = filename.split('.')[-1]
        try:
            os.mkdir(NewFiles1)
        except FileExistsError:
            pass
        print("{}/{}".format(NewFiles1, filename))
        os.rename(filename, "{}/{}".format(NewFiles1, filename))


main()
