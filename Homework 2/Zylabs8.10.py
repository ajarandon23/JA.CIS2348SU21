# Jarandon Adams - 1812590
# Zylabs 8.10

if __name__ == '__main__':
    user_input = input('Enter word here:')
    normal = ""
    reverse = ""
    for word in user_input.lower():
        if word != ' ':
            normal += word
            reverse = word + reverse
    if normal == reverse:
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")
