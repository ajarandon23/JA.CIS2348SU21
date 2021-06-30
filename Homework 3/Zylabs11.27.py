# Jarandon Adams - 1812590
# Zylabs 11.27

team_dict = {}
i = 1
count = 1

for i in range(1, 6):

    jersey_num = int(input('Enter player {}\'s jersey number:\n' .format(i)))
    rating = int(input('Enter player {}\'s rating:\n' .format(i)))
    print()

    if 0 > jersey_num > 99 or 0 > rating > 9:
        print('invalid entry')
        break

    else:
        team_dict[jersey_num] = rating

print("ROSTER")

for jersey_num, rating in sorted(team_dict.items()):

    print("Jersey number: %d, Rating: %d" % (jersey_num, rating))

option = ''

while option.upper() != 'Q':

    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')

    option = input('Choose an option:\n')

    if option == 'a':
        jersey_num = int(input('Enter a new player\'s jersey number:\n' .format(i)))
        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        team_dict[jersey_num] = rating

    elif option == 'd':
        jersey_num = int(input('Enter a jersey number:\n'))

        if jersey_num in team_dict.keys():
            del team_dict[jersey_num]

    elif option == 'u':
        jersey_num = int(input('Enter a jersey number:\n'))

        if jersey_num in team_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            team_dict[jersey_num] = rating

    elif option == 'r':
        rating_input = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))

        for jersey_num, rating in sorted(team_dict.items()):

            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_num, rating))

    elif option == 'o':
        print("ROSTER")

        for jersey_num, rating in sorted(team_dict.items()):

            print("Jersey number: %d, Rating: %d" % (jersey_num, rating))
