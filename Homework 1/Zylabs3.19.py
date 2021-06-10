# Jarandon Adams - 1812590
# Zylabs 1.12

color_dict = {
    'red': 35,
    'blue': 25,
    'green': 23
}
wallheight = float(input('Enter wall height (feet):\n'))
wallwidth = float(input('Enter wall width (feet):\n'))

area = wallwidth * wallheight
paintneeded = area / 350
paintcans = round(paintneeded)

print("Wall area:", round(area), "square feet")
print("Paint needed:", '{:.2f}'.format(paintneeded), "gallons")
print("Cans needed:", paintcans, "can(s)\n")

paintcolor = input("Choose a color to paint the wall:\n")

print("Cost of purchasing", paintcolor, "paint: $" + str(paintcans*color_dict[paintcolor]))

