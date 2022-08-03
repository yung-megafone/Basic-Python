def quick_sort(sequence):
    length = len(sequence)

    if length <= 1: #   Allows us to skip over sequences that have a length of 1 or 0
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 1, 0, 4, 3, 6, 5, 8, 9, 2, 3, 7]))
