# Jarandon Adams - 1812590
# Zylabs 6.17

password = input('Enter Password:')
encrypted_password = ''

for letter in password:
    if letter == 'i':
        encrypted_password += '!'
    elif letter == 'a':
        encrypted_password += '@'
    elif letter == 'm':
        encrypted_password += 'M'
    elif letter == 'B':
        encrypted_password += '8'
    elif letter == 'o':
        encrypted_password += '.'
    else:
        encrypted_password += letter

print(encrypted_password + 'q*s')
