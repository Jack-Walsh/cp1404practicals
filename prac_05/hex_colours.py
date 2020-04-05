HEX_COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4"}

colour = input("Enter name of colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid colour name!")
    break