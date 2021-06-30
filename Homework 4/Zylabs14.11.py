# Jarandon Adams - 1812590
# Zylabs 14.11

def selection_sort_descend_trace(lst):
    for i in range(len(lst) - 1):
        largest_value_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[largest_value_index]:
                largest_value_index = j
        lst[i], lst[largest_value_index] = lst[largest_value_index], lst[i]
        for x in lst:
            print(x, end=' ')
        print()
    return lst
