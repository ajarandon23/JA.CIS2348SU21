# Jarandon Adams - 1812590
# Zylabs 14.11

def selection_sort_descend_trace(int_list):
    for x in range(len(int_list) - 1):
        largest_value_index = x
        for y in range(x + 1, len(int_list)):
            if int_list[y] > int_list[largest_value_index]:
                largest_value_index = y
        int_list[x], int_list[largest_value_index] = int_list[largest_value_index], int_list[x]
        for z in int_list:
            print(z, end=' ')
        print()
    return int_list


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)