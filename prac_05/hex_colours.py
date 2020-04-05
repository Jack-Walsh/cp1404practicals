HEX_COLOURS = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "azure1": "#f0ffff", "azure2": "#e0eeee",
               "azure3": "#c1cdcd", "azure4": "#838b8b", "beige": "#f5f5dc", "bisque1": "#ffe4c4", "bisque2": "#eed5b7"}

for colour in HEX_COLOURS:
    print("{}".format(colour))

colour = input("Enter name of colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(HEX_COLOURS[colour])
    else:
        print("Invalid colour name!")
    break
