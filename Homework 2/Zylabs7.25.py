# Jarandon Adams - 1812590
# Zylabs 7.25

def exact_change(user_total):
    num_dollars = user_total // 100
    user_total %= 100

    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input('Enter dollar/change amount as whole integer:'))
    amt_dollars, amt_quarters, amt_dimes, amt_nickels, amt_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')

    else:
        if amt_dollars == 1:
            print('%d dollar' % amt_dollars)
        elif amt_dollars > 1:
            print('%s dollars' % amt_dollars)

        if amt_quarters > 1:
            print('%d quarters' % amt_quarters)
        elif amt_quarters == 1:
            print('%d quarter' % amt_quarters)

        if amt_dimes > 1:
            print('%d dimes' % amt_dimes)
        elif amt_dimes == 1:
            print('%d dime' % amt_dimes)

        if amt_nickels > 1:
            print('%d nickels' % amt_nickels)
        elif amt_nickels == 1:
            print('%d nickel' % amt_nickels)

        if amt_pennies > 1:
            print('%d pennies' % amt_pennies)
        elif amt_pennies == 1:
            print('%d penny' % amt_pennies)
