def get_second_smallest_nr(nr_list):
    # mutating arguments in functions is a bad practice and should be avoided
    nr_list.sort()
    minimum = nr_list[0]
    for item in nr_list[1:]:
        if item != minimum:
            return item


numbers = [6, 2, 1, 7, 9, 1, 3, 5, 2, 1]
nr = get_second_smallest_nr(numbers)
print(nr)  # result is ok
print(numbers)  # but elements in original list were reordered
