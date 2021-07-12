# Jarandon Adams - 1812590
# Zylabs 14.13

num_calls = 0


def partition(users_ids, x, y):
    btm = (x - 1)
    mid = (x + y) // 2
    pivot = users_ids[mid]
    users_ids[mid], users_ids[y] = users_ids[y], users_ids[mid]

    for z in range(x, y):
        if users_ids[z] <= pivot:
            btm = btm + 1
            users_ids[btm], users_ids[z] = users_ids[z], users_ids[btm]
    users_ids[btm + 1], users_ids[y] = users_ids[y], users_ids[btm + 1]

    return btm + 1


def quicksort(users_ids, x, y):
    global num_calls
    num_calls += 1
    if x < y:
        pivot_index = partition(users_ids, x, y)
        quicksort(users_ids, x, pivot_index - 1)
        quicksort(users_ids, pivot_index + 1, y)


if __name__ == "__main__":
    user_ids = []
    user_id_input = input()
    while user_id_input != "-1":
        user_ids.append(user_id_input)
        user_id_input = input()

    quicksort(user_ids, 0, len(user_ids) - 1)
    print(num_calls)

    for user_id_input in user_ids:
        print(user_id_input)
