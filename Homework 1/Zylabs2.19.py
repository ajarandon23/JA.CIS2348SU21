# Jarandon Adams - 1812590
# Zylabs 1.12

clemonjuice = float(input('Enter amount of lemon juice (in cups):\n'))
cwater = float(input('Enter amount of water (in cups):\n'))
cagavenectar = float(input('Enter amount of agave nectar (in cups):\n'))
amount_servings = float(input('How many servings does this make?\n'))

print("\nLemonade ingredients - yields", '{:.2f}'.format(amount_servings), "servings")
print('{:.2f}'.format(clemonjuice), "cup(s) lemon juice")
print('{:.2f}'.format(cwater), "cup(s) water")
print('{:.2f}'.format(cagavenectar), "cup(s) agave nectar")

rservings = float(input("\nHow many servings would you like to make?\n"))

clemonjuice = ((clemonjuice / amount_servings) * rservings)
cwater = ((cwater / amount_servings) * rservings)
cagavenectar = ((cagavenectar / amount_servings) * rservings)
amount_servings = rservings

print("\nLemonade ingredients - yields", '{:.2f}'.format(rservings), "servings")
print('{:.2f}'.format(clemonjuice), "cup(s) lemon juice")
print('{:.2f}'.format(cwater), "cup(s) water")
print('{:.2f}'.format(cagavenectar), "cup(s) agave nectar")

print("\nLemonade ingredients - yields", '{:.2f}'.format(rservings), "servings")
print('{:.2f}'.format(clemonjuice / 16), "gallon(s) lemon juice")
print('{:.2f}'.format(cwater / 16), "gallon(s) water")
print('{:.2f}'.format(cagavenectar / 16), "gallon(s) agave nectar")
