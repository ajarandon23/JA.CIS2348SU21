# Jarandon Adams - 1812590
# Zylabs 12.7

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    else:
        raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    return 0.7 * (220 - age)  # calculates the fat-burning heart rate


if __name__ == '__main__':
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")

    except ValueError as value:
        print(value.args[0])
        print("Could not calculate heart rate info.\n")
